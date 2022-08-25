# Tech News
The news to be scraped will be available on the _Trybe Blog_: https://blog.betrybe.com.
  These news will be saved to the database using the python functions in the `database.py` module

## Guidelines

  1. Clone the repository
  - Enter the repository folder you just cloned:
  2. Create the virtual environment for the project

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Install dependencies

  - `python3 -m pip install -r dev-requirements.txt`

  

  <strong>MongoDB</strong>

  To carry out this project, we will use a database called `tech_news`.
  News will be stored in a collection called `news`.
  There are already some functions ready in the `tech_news/database.py` file that will help you in the development.
  Do not change the functions of this file; changes to it will not be performed in the auto-evaluator.

  Run MongoDB via Docker:
  <code>docker-compose up -d mongodb</code> in the terminal.
  For more details about mongo with docker, look at the `docker-compose.yml` file

  If you want to install and run the native MongoDB server on the machine, follow the instructions in the official tutorial:

  Ubuntu: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
  MacOS: https://docs.mongodb.com/guides/server/install/
  
  With the database running, our module will be able to access it without any problems. Import the `tech_news/database.py` module and call the functions it contains.
  Remember that mongoDB will default to port 27017. If there is already another service using this port, consider disabling it.




---



# Menu:

This function is the program menu. Through it it is possible to operate the functionalities. It is an options menu, in which each option asks for the necessary information to trigger an action.

- The text displayed by the menu:
```
Select one of the following options:
 0 - Populate the bank with news;
 1 - Search for news by title;
 2 - Search for news by date;
 3 - Search for news by tag;
 4 - Search for news by category;
 5 - List top 5 news;
 6 - List top 5 categories;
 7 - Leave.
```



  <strong>
    Manual test
  </strong>
  
  Inside a virtual environment, to interact with the menu, type the command:
  
  `tech-news-analyzer`
<hr/>
<hr/>
<br/>
<hr/>
# Tech News [PORTUGUESE]
As notícias a serem raspadas estarão disponíveis no _Blog da Trybe_: https://blog.betrybe.com.
  Essas notícias serão ser salvas no banco de dados utilizando as funções python no módulo `database.py`

## Orientações

  1. Clone o repositório
  - Entre na pasta do repositório que você acabou de clonar:
  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

  

  <strong>MongoDB</strong>

  Para a realização deste projeto, utilizaremos um banco de dados chamado `tech_news`.
  As notícias serão armazenadas em uma coleção chamada `news`.
  Já existem algumas funções prontas no arquivo `tech_news/database.py` que te auxiliarão no desenvolvimento.
  Não altere as funções deste arquivo; mudanças nele não serão executadas no avaliador automático.

  Rodar MongoDB via Docker:
  <code>docker-compose up -d mongodb</code> no terminal. 
  Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

  Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:

  Ubuntu: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
  MacOS:  https://docs.mongodb.com/guides/server/install/
  
  Com o banco de dados rodando, o nosso módulo conseguirá acessá-lo sem problemas. Importe o módulo `tech_news/database.py` e chame as funções contidas nele.
  Lembre-se de que o mongoDB utilizará por padrão a porta 27017. Se já houver outro serviço utilizando esta porta, considere desativá-lo.




---



# Menu:

Esta função é o menu do programa. Através dele é possivel operar as funcionalidades.É um menu de opções, em que cada opção pede as informações necessárias para disparar uma ação.

- O texto exibido pelo menu:
```
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
```



  <strong>
    Teste manual
  </strong>
  
  Dentro de um ambiente virtual, para interagir com o menu digite o comando:
  
  `tech-news-analyzer`
