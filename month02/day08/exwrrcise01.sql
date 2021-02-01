编写一个函数，传入两个学生的ID
返回这两个学生的分数之差

delimiter $$
create function st4(uid1 int,uid2 int)
returns int
begin
declare a int;
declare b int;
set a=(select score from cls where id=uid1);
set b=(select score from cls where id=uid2);
return a-b;
end $$

