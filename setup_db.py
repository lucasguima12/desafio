import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os

# Configuração do banco de dados

DATABASE_URL = os.environ.get('DATABASE_URL')

def load_and_push_data(engine):
    # Carregar os dados dos arquivos CSV e Excel

    fake_position_path = os.environ.get('FAKE_POSITION_PATH')
    fake_allocation_path = os.environ.get('FAKE_ALLOCATION_PATH')

    df_posicoes = pd.read_csv(fake_position_path)
    df_politicas = pd.read_excel(fake_allocation_path)
    # dropando registros sem account_suitability ou class_name.

    df_posicoes.dropna(subset=['account_suitability', 'class_name'], inplace=True)

    # renomeando as colunas para terem o mesmo nome da tabela fake_position

    df_politicas.rename(columns={'Classe': 'class_name',
                                 'Conservador': 'conservador',
                                 'Moderado Conservador': 'moderado-conservador',
                                 'Moderado': 'moderado',
                                 'Moderado Agressivo': 'moderado-agressivo',
                                 'Agressivo': 'agressivo'}, inplace=True)

    # reestruturando o dataframe, para melhor vizualizaçao dos dados. A função abaixo define uma variavel como identificadora,
    # sendo a class_name, e define as outras colunas como variaveis.

    df_politicas_melted = df_politicas.melt(id_vars=['class_name'],
                                            value_vars=['conservador', 'moderado-conservador', 'moderado',
                                                        'moderado-agressivo', 'agressivo'],
                                            var_name='account_suitability', value_name='valor_alvo')
    # agora vamos agrupar o dataframe, sendo as colunas account_code, class_name e account_suitability como colunas de referencia,
    # e tabem agregar uma nova coluna, sendo ela a soma da position_value de cada agrupamento.
    agg_df = df_posicoes.groupby(['account_code', 'class_name', 'account_suitability']).agg(
        total_position_value=('position_value', 'sum')).reset_index()

    # calculando o total de cada conta (account_code).
    total_per_account = agg_df.groupby('account_code').agg(total_value=('total_position_value', 'sum'))

    # juntando o dataframe agregado com o total por conta para calcular a porcentagem de cada class_name.
    agg_df = agg_df.merge(total_per_account, on='account_code', how='left')
    agg_df['percent_of_total'] = agg_df['total_position_value'] / agg_df['total_value']

    # Agora, vamos fazer um merge da tabela agg_df com df_politicas_melted usando account_suitability e class_name como chaves
    merged_df = agg_df.merge(df_politicas_melted, on=['account_suitability', 'class_name'], how='left').fillna(0)

    #### criando uma coluna para distancia, dividindo o total da porcentagem pelo valor alvo e elevando ao quadrado.

    merged_df['distancia'] = (merged_df['percent_of_total'] - merged_df['valor_alvo']) ** 2

    # criando um dataframe com a soma da distancia de cada account_code.

    df_final = merged_df.groupby('account_code')['distancia'].sum().reset_index()

    # com isso, aplicamos a raiz quadrada para termos a distancia euclidiana.

    df_final['distancia'] = df_final['distancia'].apply(np.sqrt)


    df_final.to_sql('distancia_euclidiana', engine, if_exists='replace', index=False)
    df_posicoes.to_sql('posicoes', engine, if_exists='replace', index=False)
    df_politicas.to_sql('politicas', engine, if_exists='replace', index=False)

def main():
    # Criar um engine de banco de dados
    engine = create_engine(DATABASE_URL)

    # Carregar os dados e subir as tabelas no banco
    load_and_push_data(engine)

if __name__ == '__main__':
    main()
