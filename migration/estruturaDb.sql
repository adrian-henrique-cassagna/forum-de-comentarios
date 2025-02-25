create database if not exists db_feedback;

use db_feedback;

create table if not exists tb_comentarios(
	id_comentario int primary key AUTO_INCREMENT, 
	data_hora datetime,
    nome varchar(30) not null,
    comentario text);
    
select * from tb_comentarios