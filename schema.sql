create database series_db;

create table Usuario(
    cod serial,
    nome varchar(100),
    login varchar(50),
    altura numeric,
    idade integer,
    email varchar(50),
    senha varchar(500)
);