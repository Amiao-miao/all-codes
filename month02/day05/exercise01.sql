create table book(id int primary key auto_increment,
                  title varchar(50) not null,
                  author varchar(20) not null,
                  publishing_company varchar(50) not null,
                  price decimal(6,2) not null,
                  remark text
);

insert into book(title,author,publishing_company,price,remark)
values
("《平凡的世界》","路遥","人民教育出版社",28.83,"这是一部全景式地表现中国当代城乡社会生活的长篇小说。全书共三部。"),
("《穆斯林的葬礼》","霍达","人民教育出版社",25.3,"一个穆斯林的家族，六十年间的兴衰，三代人命运的沉浮，两个发生在不同时代、有着不同内容却又交错扭结的爱情悲剧。"),
("《挪威的森林》","村上春树","中国大百科出版社",32.97,"一本风靡全亚洲百分之百的恋爱小说，曾高居日本文学史上的“超级畅销书”。"),
("《基督山伯爵》","大仲马","法国文学",31.4,"法国著名作家大仲马的代表作。"),
("《教父》","马里奥·普佐","中国文学",23.86,"是1969年美国出版的长篇小说，是美国出版史上的头号畅销书，曾连续70周排名畅销榜，37年销量达2000万册."),
("《苏菲的世界》","乔斯坦·贾德","人民教育出版社",35.7,"风靡全球、超级畅销的哲学奇书全世界最易读懂的哲学书。"),
("《麦田里的守望者》","乔斯坦·贾德","三联书店",22.6,"是塞林格唯一的一部长篇，虽然只有十几万字，它却在美国社会上和文学界产生过巨大影响。"),
("《万历十五年》","黄仁宇","人民教育出版社",35.7,"明万历十五年，即公元1587年，在中国历史上原本是极其普通的年份。"),
("《围城》","钱钟书","三联书店",29.6,"是中现代文学史上一部风格独特的讽刺小说。"),
("《呐喊》","老舍","三联书店",32.1);


1. 将呐喊的价格修改为45元
update book set price=45 where title="《呐喊》";
2. 增加一个字段出版时间 类型为 date 放在价格后面
alter table book add publishing_time date after price;
3. 修改所有老舍的作品出版时间为 2018-10-1
update book set publishing_time="2018-10-1" where author="老舍";
4. 修改所有中国文学出版社出版的但是不是老舍的作品出版时间为 2020-1-1
update book set publishing_time="2020-1-1"
where publishing_company="中国文学出版社" and author!="老舍";
5. 修改所有出版时间为Null的图书 出版时间为 2019-10-1
update book set publishing_time="2019-10-1"
where publishing_time is null;
6. 所有鲁迅的图书价格增加5元
update book set price=price+5
where author="鲁迅";
7. 删除所有价格超过70元或者不到40元的图书
delete from book where not between 40 and 70;
