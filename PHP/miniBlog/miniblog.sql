create database miniblog;
use miniblog;
create table users(
	id TINYINT auto_increment primary key,
	username VARCHAR(20) not null,
	password VARCHAR(40) not null,
);
create table articles(
	id INT auto_increment primary key,
	dateposted VARCHAR(20) not null,
	articleTitle VARCHAR(50) not null
);
