编写一个存储过程，传入一个学生姓名，打印出这个学生的信息，并且在爱好表中加入这个学生，喜欢画画

create procedure like_draw1(in sname varchar(30))
begin

select * from cls where name=sname;
insert into hobby(name,hobby,price) values(sname,"draw",188000);

end $$