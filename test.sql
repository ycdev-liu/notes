-- Active: 1773044192198@@127.0.0.1@3306@my_app_db
show DATABASES


create database mydb

show DATABASEs

use mydb;


show DATABASES

drop DATABASE mydb

show DATABASES




use mydb

create table employees(
    id INT auto_increment primary KEY,
    name varchar(50) not NULL,
    department varchar(50),
    salary decimal(10,2),
    hrie_date DATE
);
show TABLES

drop table 

insert into employees(name,depart,salary,hire_date)
value("alice","hr",6000.00,'2022-01-15')

select * from employees;