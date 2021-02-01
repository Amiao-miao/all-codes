create table class(id int primary key auto_increment,
                   name varchar(30) not null,
                   age tinyint unsigned,sex enum('m','w','o'),
                   score float default 0);


create table hobby(id int primary key auto_increment,
                   name varchar(30) not null,
                   hobby set('sing','dance','draw') comment "选择爱好",
                   level char,
                   price decimal(7,2) not null,
                   remark text);


insert into hobby(name,hobby,level,price,remark)
values
("Lily","sing,dance","A",48800.888,"练舞奇才"),
("Bob","draw","B",8800,"当代达芬奇"),
("Jame","sing","A",24600,"天籁之音")
("Emma","dance","C",4600),
("Anna","sing","B",24600)