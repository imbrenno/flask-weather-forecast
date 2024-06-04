# Flask Weather Forecast

Este repositório contém uma estrutura básica para um projeto Flask que utiliza o MongoDB como banco de dados e Docker para a criação de contêineres. O projeto segue a arquitetura MVC (Model-View-Controller) e utiliza microserviços para modularizar as funcionalidades.


#### Arquitetura MVC (Model-View-Controller)

A estrutura do projeto segue o padrão de arquitetura MVC, que se divide em:

- **Model**: Representa os dados da aplicação, incluindo a lógica de negócio relacionada a esses dados. No diretório `main/database/models`, estão os modelos de dados da aplicação, enquanto `main/database/database.py` cuida da conexão com o MongoDB.
  
- **View**: Responsável pela interface do usuário, porém, neste projeto Flask, as views são tratadas principalmente pelos templates HTML e pelo frontend separadamente, não sendo abordadas diretamente na estrutura do código fornecida.
  
- **Controller**: Gerencia as requisições do usuário e as operações sobre os dados. No diretório `main/controllers`, estão os controladores da aplicação, que contêm as rotas e a lógica de negócio, como o arquivo `direct_geocoding_ctrl`.


#### Executando o projeto

Para executar o projeto, siga os passos abaixo:

1. Certifique-se de ter o Docker instalado em sua máquina.
2. Clone este repositório em sua máquina local.
3. Navegue até o diretório do projeto.
4. Instale o ambiente virtual com o comando`python -m venv venv`.
5. Navegue até o diretório `venv\Scripts\` e execute o arquivo `activate ou activate.bat`
5. Crie um arquivo `.env` com as configurações necessárias (baseie-se no `.env.example`).
6. Execute o comando `docker-compose up --build` para construir e iniciar os contêineres.
7. Acesse a aplicação em `http://localhost:5000` no seu navegador.



Sugestões para melhorias irão contruibuir com meu aprendizado.


By `Brenno Maia`