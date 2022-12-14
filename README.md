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

  To carry out this project, use a database called `tech_news`.
  News will be stored in a collection called `news`.

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


<br/>
<hr/>
<br/>


# Tech News [PORTUGUESE]
As not??cias a serem raspadas estar??o dispon??veis no _Blog da Trybe_: https://blog.betrybe.com.
  Essas not??cias ser??o ser salvas no banco de dados utilizando as fun????es python no m??dulo `database.py`

## Orienta????es

  1. Clone o reposit??rio
  - Entre na pasta do reposit??rio que voc?? acabou de clonar:
  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as depend??ncias

  - `python3 -m pip install -r dev-requirements.txt`

  

  <strong>MongoDB</strong>

  Para a realiza????o deste projeto, utilize o banco de dados chamado `tech_news`.
  As not??cias ser??o armazenadas em uma cole????o chamada `news`.
  
  Rodar MongoDB via Docker:
  <code>docker-compose up -d mongodb</code> no terminal. 
  Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

  Caso queira instalar e rodar o servidor MongoDB nativo na m??quina, siga as instru????es no tutorial oficial:

  Ubuntu: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
  MacOS:  https://docs.mongodb.com/guides/server/install/
  
  Com o banco de dados rodando, o nosso m??dulo conseguir?? acess??-lo sem problemas. Importe o m??dulo `tech_news/database.py` e chame as fun????es contidas nele.
  Lembre-se de que o mongoDB utilizar?? por padr??o a porta 27017. Se j?? houver outro servi??o utilizando esta porta, considere desativ??-lo.




---



# Menu:

Esta fun????o ?? o menu do programa. Atrav??s dele ?? possivel operar as funcionalidades.?? um menu de op????es, em que cada op????o pede as informa????es necess??rias para disparar uma a????o.

- O texto exibido pelo menu:
```
Selecione uma das op????es a seguir:
 0 - Popular o banco com not??cias;
 1 - Buscar not??cias por t??tulo;
 2 - Buscar not??cias por data;
 3 - Buscar not??cias por tag;
 4 - Buscar not??cias por categoria;
 5 - Listar top 5 not??cias;
 6 - Listar top 5 categorias;
 7 - Sair.
```



  <strong>
    Teste manual
  </strong>
  
  Dentro de um ambiente virtual, para interagir com o menu digite o comando:
  
  `tech-news-analyzer`
