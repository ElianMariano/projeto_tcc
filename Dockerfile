FROM postgres:12

# Define a senha
ENV POSTGRES_PASSWORD=password

# Define o nome do banco de dados
ENV POSTGRES_DB=database

# Define usuario padrão do postgre
USER postgres

EXPOSE 5435:5432