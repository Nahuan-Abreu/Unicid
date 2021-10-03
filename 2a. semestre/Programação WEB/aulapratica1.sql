CREATE TABELE VENDEDORES(
    nome  VARCHAR (50),
    ativo  BOOLEAN(0 ou 1 )/* (0 = false, 1 = true)*/
    foto  VARCHAR(25), /*(quando for foto, colocamos onde a foto esta localizada)*/
    comissao  FLOAT(5/*(quantidade maxima de caracteres)*/,2/*( E a quantidade onde o ponto vai estar, separando os numeros))*/,
    uf  CHAR(2), /*(quantidade de letras/caracteres)*/
    obs  TEXT /*(aceita ate 60 mil caracteres.)*/
);

/*CRIANDO UMA TABELA DE PRODUTOS.*/
CREATE TABLE produtos (
    codigo VARCHAR(10) ,
    nome VARCHAR(50) ,
    ativo BOOLEAN ,
    precoVenda FLOAT(6,2) , 
    foto VARCHAR(25) , 
    estoque INT(5) ,
    promocao INT(1) , /*PODEMOS TROCAR O BOOLEAN PELO INT(1). A DIFERENCA QUE O INT OCUPA MAIS ESPACO DO QUE O BOOLEAN*/
    descricao TEXT
);

/*INSERINDO VALORES*/
INSERT INTO Vendedores VALUES (
    "Roberto Carlos",
    1, 
    "foto12.png",
    25.00,
    "SP",
    "Atende Grande São Paulo (SP, Guarulhos e Osasco)"  

);
 INSERT INTO Vendedores VALUES(
    "Ana Regina",
    1,
    "foto13.png",
    22.50,
    "RJ",
    "Atende Grande rio"
);

INSERT INTO Vendedores VALUES(
    "Ana Regina",
    0,
    "foto05.png",
    12.75,
    "SC",
    "Florianópolis e região"
);
/*INSERIR UM NOVO CAMPO NA TABELA*/
ALTER TABLE Vendedores ADD COLUMN codigo INT FIRST;

/*comando para excluir uma tabela chamada codigo*/
ALTER TABLE Vendedores DROP COLUMN codigo;

/*comando que vms utilizar para ogranizar. para que os nomes fique com apenas um codigo, sem repetir.*/ 
ALTER TABLE Vendedores ADD COLUMN codigo INT AUTO_INCREMENT FIRST, ADD PRIMARY KEY(codigo)

/*trocar o nome de roberto carlos para ana regina*/
UPDATE vendedores SET nome="Ana Regina" WHERE nome="Roberto Carlos";

/*Adicionando os valores na tabela do produtos.*/
INSERT INTO produtos VALUES (
    "COD-0016DO",
    "iphone 5s 16GB Dourado",
    1,
    2653.85,
    "iPhone5s-gold.png",
    58,
    0,
    "Smartphone iPhone Apple última geração cor Dourada" 
);

INSERT INTO produtos (
    codigo,
    nome,
    ativo,
    descricao
) 
VALUES (
    "COD-0032CH",
    "iphone 5s 16GB Champagne",
    0,
    
    "Smartphone iPhone Apple última geração cor Champagne" 
);

