CREATE DATABASE set2021;

Clientes 
id (PK)    nome
1          Ana Sá
2          Carlos Majer
3          Renata Vasconcelos

Funcionários
id        nome
1         Antonio Martins
2         Marcos da Silva
3         



CREATE TABLE clientes (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nome        VARCHAR(80),
    ddd         VARCHAR(2),
    telefone    VARCHAR(11),
    endereco    TEXT,
    email       VARCHAR(100),
    conveniado  BOOLEAN,
    tipo        CHAR(1)
);


CREATE TABLE carros(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    idCliente   INT,
    placa       VARCHAR(8),
    tipo        VARCHAR(10),
    fabricante  VARCHAR(25),
    modelo      VARCHAR(25),
    ano         INT(4),
    cor         VARCHAR(15)
);

CREATE TABLE mensalidades(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    idCarro      INT,
    vencimento   DATE,
    valor        FLOAT(7,2),
    situacao     BOOLEAN,
    ativa        BOOLEAN,
    obs          TEXT
);


CREATE TABLE locacoes(
    id               INT AUTO_INCREMENT PRIMARY KEY,
    dtEntrada        DATE,
    hEntrada         CHAR(5),
    dtSaida          DATE,
    hSaida           CHAR(5),
    placa            VARCHAR(8),
    uf               CHAR(2),
    fabricante       VARCHAR(20),
    modelo           VARCHAR(20),
    cor              VARCHAR(15),
    ano              INT(4),
    valor            FLOAT(6,2),
    convenio         TINYINT (1),
    pago             BOOLEAN,
    obs              TEXT
);