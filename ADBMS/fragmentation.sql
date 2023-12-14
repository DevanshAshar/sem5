use devansh;
-- Range
create table frag (id int,name varchar(25),marks int,age int)
partition by range(marks)(
partition p0 values less than (10),
partition p1 values less than (20),
partition p2 values less than (30));
INSERT INTO frag VALUES
(1, 'John', 5, 25),
(2, 'Alice', 15, 30),
(3, 'Bob', 25, 22),
(4, 'Catherine', 8, 28),
(5, 'David', 18, 35),
(6, 'Eva', 12, 29),
(7, 'Frank', 22, 26),
(8, 'Grace', 7, 31),
(9, 'Henry', 28, 23),
(10, 'Ivy', 14, 27);
select * from frag partition(p1);
drop table frag;
-- List
create table frag (id int,name varchar(25),marks int,age int)
partition by list(id)(
partition p0 values in(1,4,7,10),
partition p1 values in(2,5,8),
partition p2 values in(3,6,9));
select * from frag partition(p2);
-- HASH
create table frag (id int,name varchar(25),marks int,age int)
partition by hash(marks)
partitions 3;
-- KEY
create table frag (id int,name varchar(25),marks int,age int,primary key(id))
partition by key()
partitions 3;
