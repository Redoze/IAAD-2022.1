create database ClinicasMedicas
default character set utf8mb4
default collate utf8mb4_general_ci;

USE ClinicasMedicas;
select database();

create table if not exists Medico (
CodMed char(7),
NomeMed varchar(40) not null,
Genero char(1),
Telefone char(16),
Email varchar(40),
CodEspec char(7), -- nome da especialidade
primary key (CodMed),
unique (Email)
) default charset = utf8mb4;
-- alter table Medico add foreign key(CodEspec) references Especialidade(CodEspec) on delete cascade on update cascade;

insert into medico
(CodMed, NomeMed, Genero, Telefone, Email, CodEspec)
values
('6699123', 'George', 'M', '(81) 93366-6633', 'george@mail.com', '4567123'),
('6611223', 'Edmundo', 'M', '(81) 93366-6633', 'edmundo@mail.com', '4567123'),
('2255668', 'Thaís', 'F', '(81) 95599-9955', 'thais@mail.com', '9922335'),
('3300990', 'Aline', 'F', '(81) 94455-8833', 'aline@mail.com', '2288995'),
('7799110', 'Gabriela', 'F', '(81) 91111-0000', 'gabriela@mail.com', '7788991'),
('9911225', 'Rafaela', 'F', '(83) 95555-9988', 'rafaela@mail.com', '8855664'),
('6677889', 'Daniel', 'M', '(81) 91122-3344', 'daniel@mail.com', '6676123'),
('6655779', 'Danilo', 'M', '(81) 97799-8855', 'danilo@mail.com', '1451689'),
('4455667', 'Ana', 'F', '(81) 98888-9900', 'ana@mail.com', '4567123'),
('3344556', 'Maria', 'F', '(81) 99977-0000', 'maria@mail.com', '1451689'),
('2233445', 'João', 'M', '(84) 98877-6655', 'joao@mail.com', '3547126'),
('1122334', 'Felipe', 'M', '(81) 98247-2791', 'felipe@mail.com', '3547126'),
('1234567', 'Carla', 'F', '(21) 99218-5763', 'carla@mail.com', '2568749'),
('1478935', 'André', 'M', '(83) 98772-3348', 'andre@mail.com', '2568749'),
('5566778', 'Joaquim', 'M', '(83) 97777-5563', 'joaquim@mail.com', '2568749'),
('1100556', 'Beatriz', 'F', '(83) 98855-8855', 'beatriz@mail.com', '4567123'),
('1582103', 'Laura', 'F', '(11) 99524-0127', 'laura@mail.com', '1451689'),
('1314156', 'Socorro', 'F', '(83) 97788-0025', 'socorro@mail.com', '3547126'),
('7788990', 'Thiago', 'M', '(84) 97589-9999', 'thiago@mail.com', '3547126'),
('8877990', 'Pedro', 'M', '(81) 90099-9933', 'pedro@mail.com', '3547126');

select * 
from medico;

describe medico;

create table if not exists Especialidade (
CodEspec char(7),
NomeEspec varchar(15),
Descricao text not null,
primary key (CodEspec)
) default charset = utf8mb4;

insert into especialidade
(CodEspec, NomeEspec, Descricao)
values
('6676123', 'Psiquiatria', 'doenças mentais'),
('7788991', 'Psicologia', 'estudo dos processos mentais'),
('8855664', 'Oftalmologista', 'doenças nos olhos'),
('9922335', 'Odontologista', 'tratamento dos dentes'),
('2288995', 'Ginecologista', 'saúde da mulher'),
('3547126', 'Cardiologia', 'doenças do coração'),
('2568749', 'Dermatologia', 'doenças da pele'),
('1451689', 'Pediatria', 'doenças da criança'),
('4567123', 'Endocrinologia', 'doenças das gândulas'),
('5676321', 'Otorrino', 'doenças nariz, ouvido, garganta');

select *
from especialidade;

describe especialidade;

show databases;

