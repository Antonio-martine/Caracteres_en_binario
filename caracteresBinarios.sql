show databases;
create database if not exists caracter_binario;
use caracter_binario;
create table if not exists minusculas(
id_minusculas int primary key not null auto_increment,
letra varchar(3) not null,
conversion varchar(8) not null
)ENGINE=InnoDB;

create table if not exists mayusculas(
id_mayusculas int primary key not null auto_increment,
letra varchar(3) not null,
conversion varchar(8) not null
)ENGINE=InnoDB;

create table if not exists numeros(
id_numero int primary key not null auto_increment,
numero int not null,
conversion varchar(8) not null
)ENGINE=InnoDB;

show tables;

insert into minusculas(letra,conversion) values ('a','01100001'),
('b','01100010'),('c','01100011'),('d','01100100'),('e','01100101'),('f','01100110'),
('g','01100111'),('h','01101000'),('i','01101001'),('j','01101010'),('k','01101011'),
('l','01101100'),('m','01101101'),('n','01101110'),('o','01101111'),('p','01110000'),
('q','01110001'),('r','01110010'),('s','01110011'),('t','01110100'),('u','01110101'),
('v','01110110'),('w','01110111'),('x','01111000'),('y','01111001'),('z','01111010');
select * from minusculas;

insert into mayusculas(letra,conversion) values ('A','01000001'),
('B','01000010'),('C','01000011'),('D','01000100'),('E','01000101'),('F','01000110'),
('G','01000111'),('H','01001000'),('I','01001001'),('J','01001010'),('K','01001011'),
('L','01001100'),('M','01001101'),('N','01001110'),('O','01001111'),('P','01010000'),
('Q','01010001'),('R','01010010'),('S','01010011'),('T','01010100'),('U','01010101'),
('V','01010110'),('W','01010111'),('X','01011000'),('Y','01011001'),('Z','01011010');
select * from mayusculas;

insert into numeros (numero, conversion) values (1,'00110001'),(2,'00110010'),
(3,'00110011'),(4,'00110100'),(5,'00110101'),(6,'00110110'),(7,'00110111'),
(8,'00111000'),(9,'00111001'),(0,'00110000');
select * from numeros;

Select conversion from minusculas;


