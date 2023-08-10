# Sistema de Aderência de Política de Investimentos

- Sistema para auxiliar a gestora de carteira **** a determinar a aderência das contas dos clientes às suas respectivas políticas de investimentos.

## Index

- [Pré-requisitos](#Pré-requisitos)
- [Instalação](#Instalação)
- [Configuração](#Configuração)
- [Uso](#Uso)  
- [Dashboard](#Dashboard)


## Pré-requisitos
### Python 3.8 ou superior.
[Link para instalação](https://www.python.org/downloads/)
### Bibliotecas
Para instalar, execute os seguintes comandos no CMD:
   #### pip install pandas
   #### pip install sqlalchemy
   #### pip install psycopg2
   #### pip install openpyxl
### PostgreSQL 13 ou superior.
[Link para instalação](https://www.postgresql.org/download/)

## Instalação:

#### git clone [link do repositorio]
#### cd [nome do diretório do projeto]

## Configuração
## Configurando o Banco de Dados
#### Antes de iniciar a aplicação, você deve configurar o banco de dados, criando um servidor PostgreSQL e criando um database. 
#### Apos isto, será necessário definir uma variável de ambiente chamada DATABASE_URL que aponte para a sua instância PostgreSQL.

## No Windows (Prompt de Comando):

#### set DATABASE_URL=postgresql://[seu_usuario]:[sua_senha]@localhost/[nome_do_db]

## No Linux ou MacOS (Terminal):

#### export DATABASE_URL=postgresql://[seu_usuario]:[sua_senha]@localhost/[nome_do_db]

- Substitua [seu_usuario], [sua_senha] e [nome_do_db] pelas informações apropriadas da sua instância PostgreSQL.

## Configurando Caminhos dos Arquivos
#### O script espera por dois arquivos de dados: fake_position.csv e fake_allocation_policies.xlsx. Se você os moveu para um local diferente da raiz do projeto, precisará informar seus novos caminhos usando as variáveis de ambiente fake_position_path e fake_allocation_path.

## No Windows (Prompt de Comando):

#### set FAKE_POSITION_PATH=/path/to/fake_position.csv
#### set FAKE_ALLOCATION_PATH=/path/to/fake_allocation_policies.xlsx

## No Linux ou MacOS (Terminal):

#### export FAKE_POSITION_PATH=/path/to/fake_position.csv
#### export FAKE_ALLOCATION_PATH=/path/to/fake_allocation_policies.xlsx

- Substitua /path/to/fake_position.csv e /path/to/fake_allocation_policies.xlsx pelos caminhos reais dos seus arquivos.

## Uso

1. Execute o script setup_db.py para rodar o codigo e alimentar o banco de dados com as tabelas.
2. Para acesar as tabelas:
   1. Utilizando pgAdmin:
      Inicie o pgAdmin.
        Conecte-se ao servidor usando as credenciais fornecidas anteriormente (ou as padrões se você não as alterou).
Expanda o servidor e selecione o banco de dados [nome_do_db] (ou o nome que você forneceu durante a configuração).
Dentro do banco de dados, expanda a seção "Esquemas", depois "public" e depois "Tabelas". Aqui você verá as tabelas que foram carregadas pelo script.
   2. Utilizando a Linha de Comando (psql): Inicie o terminal ou prompt de comando.
Conecte-se ao PostgreSQL usando o comando:
#### psql -U [seu_usuario] -h localhost -d [nome_do_db]

Após estar conectado, você pode listar todas as tabelas com:
#### \dt

Para consultar os dados de uma tabela específica, por exemplo, nome_da_tabela, use:
#### SELECT * FROM nome_da_tabela;
3. Outra forma de acesso é pelo notebook Desafio.ipynb, precisando somente alterar o servidor do Postgre e os paths de cada arquivo csv.

## Dashboard

[Link para o dashboard](https://app.powerbi.com/groups/me/reports/5ea33c04-3304-468f-b0bd-0ff4138e3584/ReportSection?experience=power-bi)

Print:

![Screenshot_1](Screenshot_1.png)











