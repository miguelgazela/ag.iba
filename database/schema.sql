drop table if exists utilizador;
drop table if exists cliente;
drop table if exists imposto;
drop table if exists actividade;

create table utilizador (
	id_utilizador integer primary key autoincrement,
	username text,
	pass_hash text,
	tipo integer
);

create table cliente (
	id_cliente integer primary key autoincrement,
	nome text,
	morada text,
	cidade text,
	freguesia text,
	cod_postal text,
	nif text,
	tipo integer
);

create table imposto (
	id_imposto integer primary key autoincrement,
	id_cliente not null references clientes(id_cliente),
	marca text,
	modelo text,
	matricula text,
	data_matricula date,
	data_pagamento date,
	tipo integer
);

create table actividade (
	id_actividade integer primary key autoincrement,
	id_utilizador not null references utilizadores(id_utilizador),
	id_cliente references clientes(id_cliente),
	id_imposto references impostos(id_imposto),
	tipo integer,
	descricao text,
	data_alteracao date
);