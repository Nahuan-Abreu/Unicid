CREATE DATABASE Set2021;

USE Set2021;

CREATE TABLE clientes (
	id  	   	INT   AUTO_INCREMENT   PRIMARY   KEY 	,
	nome	   	VARCHAR (80) 		    				,
	ddd 	   	VARCHAR (2) 		    				,
	telefone 	VARCHAR (11) 							, 
	endereco 	TEXT 									,
	email  	   	VARCHAR (100) 		    				,
	conveniado 	BOOLEAN			    					,
	tipo	   	CHAR (1)
);

CREATE TABLE carros (
	id  		INT AUTO_INCREMENT PRIMARY KEY  ,
	idCliente  	INT				  				,
	placa	 	VARCHAR(8)			  			,
	tipo  		VARCHAR(10)			  			,
	fabricante  VARCHAR(25) 			  		,
 	modelo  	VARCHAR(25) 			  		,
	ano   		INT(4)				  			,
	cor   		VARCHAR(15)
);


CREATE TABLE mensalidades (
	id  	  	INT AUTO_INCREMENT PRIMARY KEY  ,
	idCarro	  	INT								,
	vencimento  DATE							,
	valor 	  	FLOAT(7,2)						,
	situacao  	BOOLEAN							, 
	ativa 	  	BOOLEAN							,
	obs 	  	TEXT
);

CREATE TABLE locacoes (
    id   		INT AUTO_INCREMENT PRIMARY KEY 	,
	dtEntrada  	DATE							,
	hEntrada  	CHAR (5)			 			,
	dtSaida  	DATE							,
	hSaida 	 	CHAR (5)			 			,
	placa 	 	VARCHAR (8)						,
	uf    	 	CHAR (2)				 		,
	fabricante  VARCHAR (20)					,
	modelo 	 	VARCHAR (20)					,
	cor 	 	VARCHAR (15)					,
	ano 	 	INT (4)							,
	valor  	 	FLOAT (6,2)						,
	convenio  	TINYINT (1)						,
  	pago 	 	BOOLEAN			 				,
 	obs 	 	TEXT
);

INSERT INTO clientes VALUES 
(
	0	         ,
	"Thabata Souza"      ,
	"11"	         ,
	"2012-3456"	         ,
	"rua a, número 1"    ,
	"thabat@email.com.br",
	0	        ,
	"M"
) ;

INSERT INTO clientes VALUES 
(
	0	,
	"Gustavo Vicente",
	"11"	,
	"5331-1010"	,
	"av. b, número 2",
	"gustavo@email.com.br",
	0,
	"E"
) ;

INSERT INTO clientes VALUES 
(
	0	 ,
	"vinicius alves" ,
	"11"	 ,
	"99123-4567"	 ,
	"pça sem número, escondida" ,
	"vinicius@email.com.br"	,
	1		,
	"M"
) ;

INSERT INTO carros VALUES 
(
	0	,
	1	,
	"ABC-1234"	,
	"SUV"	,
	"VW"	,
	"T-CROSS"	,
	2020 	,
	 "Prata"
) ;

INSERT INTO carros VALUES 
(
	0	,
	3	,
	"XYZ-0001"	,
	"HATCH"	,
	"Fiat"	,
	"Palio"	,
	2006 	,
	 "Preta"
) ;

INSERT INTO carros VALUES 
(CREATE DATABASE Set2021;

USE Set2021;

CREATE TABLE clientes (
	id  	   	INT   AUTO_INCREMENT   PRIMARY   KEY 	,
	nome	   	VARCHAR (80) 		    				,
	ddd 	   	VARCHAR (2) 		    				,
	telefone 	VARCHAR (11) 							, 
	endereco 	TEXT 									,
	email  	   	VARCHAR (100) 		    				,
	conveniado 	BOOLEAN			    					,
	tipo	   	CHAR (1)
);

CREATE TABLE carros (
	id  		INT AUTO_INCREMENT PRIMARY KEY  ,
	idCliente  	INT				  				,
	placa	 	VARCHAR(8)			  			,
	tipo  		VARCHAR(10)			  			,
	fabricante  VARCHAR(25) 			  		,
 	modelo  	VARCHAR(25) 			  		,
	ano   		INT(4)				  			,
	cor   		VARCHAR(15)
);


CREATE TABLE mensalidades (
	id  	  	INT AUTO_INCREMENT PRIMARY KEY  ,
	idCarro	  	INT								,
	vencimento  DATE							,
	valor 	  	FLOAT(7,2)						,
	situacao  	BOOLEAN							, 
	ativa 	  	BOOLEAN							,
	obs 	  	TEXT
);

CREATE TABLE locacoes (
    id   		INT AUTO_INCREMENT PRIMARY KEY 	,
	dtEntrada  	DATE							,
	hEntrada  	CHAR (5)			 			,
	dtSaida  	DATE							,
	hSaida 	 	CHAR (5)			 			,
	placa 	 	VARCHAR (8)						,
	uf    	 	CHAR (2)				 		,
	fabricante  VARCHAR (20)					,
	modelo 	 	VARCHAR (20)					,
	cor 	 	VARCHAR (15)					,
	ano 	 	INT (4)							,
	valor  	 	FLOAT (6,2)						,
	convenio  	TINYINT (1)						,
  	pago 	 	BOOLEAN			 				,
 	obs 	 	TEXT
);

INSERT INTO clientes VALUES 
(
	0	         ,
	"Thabata Souza"      ,
	"11"	         ,
	"2012-3456"	         ,
	"rua a, número 1"    ,
	"thabat@email.com.br",
	0	        ,
	"M"
) ;

INSERT INTO clientes VALUES 
(
	0	,
	"Gustavo Vicente",
	"11"	,
	"5331-1010"	,
	"av. b, número 2",
	"gustavo@email.com.br",
	0,
	"E"
) ;

INSERT INTO clientes VALUES 
(
	0	 ,
	"vinicius alves" ,
	"11"	 ,
	"99123-4567"	 ,
	"pça sem número, escondida" ,
	"vinicius@email.com.br"	,
	1		,
	"M"
) ;

INSERT INTO carros VALUES 
(
	0	,
	1	,
	"ABC-1234"	,
	"SUV"	,
	"VW"	,
	"T-CROSS"	,
	2020 	,
	 "Prata"
) ;

INSERT INTO carros VALUES 
(
	0	,
	3	,
	"XYZ-0001"	,
	"HATCH"	,
	"Fiat"	,
	"Palio"	,
	2006 	,
	 "Preta"
) ;

INSERT INTO carros VALUES 
(
	0		,
	1		,
	"BB-899"		,
	"Moto"		,
	"Honda"		,
	"CB-500"		,
	1989 		,
	 "Amarela"
) ;

SELECT * FROM locacoes;

	0		,
	1		,
	"BB-899"		,
	"Moto"		,
	"Honda"		,
	"CB-500"		,
	1989 		,
	 "Amarela"
) ;


INSERT INTO locacoes VALUES
(1,	"2021-09-14",	"22:55",	NULL		,	"",			"ABC-1234",	"RS",	"VW"	 ,	"Gol GTI",	"Prata"	,	1999,	0	 ,	0,			0,		"") 			 	,
(2,	"2021-09-14",	"23:00",	"2021-09-15",	"08:00",	"XYZ-0000",	"SP",	"Fiat"	 ,	"Strada" ,	"Preta"	,	1985,	40.00,	0,			1,		"Taxa Pernoite") 	,
(3,	"2021-09-15",	"08:15",	NULL		,	"",			"NBC-0101",	"RJ",	"Honda"	 ,	"HRV"	 ,	"Branca",	2019,	0	 ,	0,			0,		"")					,
(4,	"2021-09-15",	"08:20",	"2021-09-15",	"08:45",	"GXS-0009",	"SC",	"Ford"	 ,	"Ká"	 ,	"Azul"	,	2014,	8.00 ,	0,			0,		"Pendente / conta")	,
(5,	"2021-09-15",	"08:23",	"2021-09-15",	"09:00",	"GAF-1001",	"SP",	"Hiunday",	"I30"	 ,	"Prata"	,	2011,	28.00,	1,			1,		"Lavagem simples")	,
(6,	"2021-09-15",	"08:40",	NULL		,	"",			"FAL-9803",	"SP",	"GM"	 ,	"Tracker",	"Verde"	,	2020,	0	 ,	1,			0,		"")					,
(7,	"2021-09-15",	"08:55",	NULL		,	"",			"ESC-1055",	"SP",	"Peugeot",	"206"	 ,	"Branca",	2015,	0	 ,	0,			0,		"")					,
(8,	"2021-09-15",	"09:01",	NULL		,	"",			"BLW-1500",	"SP",	"VW"	 ,	"Fusca"	 ,	"Verde"	,	1970,	0	 ,	0,			0,		"",) ;

SELECT * FROM locacoes;







