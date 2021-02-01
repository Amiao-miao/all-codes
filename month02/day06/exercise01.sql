1. 查找所有蜀国人信息，按照攻击力排名
select * from sanguo where country="蜀" order by attack desc;
2. 将赵云攻击力设置为360，防御设置为70
update sanguo set attack=360,defense=70 where name="赵云";
3. 吴国英雄攻击力超过300的改为300，最多改2个
update sanguo set attack=300 where attack>300 and country="吴" limit 2;
4. 查找攻击力超过200的魏国英雄名字和攻击力并显示为姓名， 攻击力
select name as 姓名,attack as 攻击力 from sanguo where attack>200 and country="魏";
5. 所有英雄按照攻击力降序排序，如果相同则按照防御生序排序
select * from sanguo order by attack desc,defense;
6. 查找名字为3字的
select * from sanguo where name like "___";
7. 查找攻击力比魏国最高攻击力的人还要高的蜀国英雄
select * from sanguo
where country="蜀"
and attack>(select attack from sanguo where country="魏" order by attack desc limit 1);
8. 找到魏国防御力排名2-3名的英雄
select * from sanguo where country="魏" order by defense desc  limit 2 offset 1;
9. 查找所有女性角色中攻击力大于180的和男性中攻击力小于250的
select * from sanguo where gender="女" and attack>180
union select * from sanguo where attack<250 and gender="男";
