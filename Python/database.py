import mysql.connector as msc
cnx = msc.connect(user='root', password='Mysql@123', host="127.0.0.1", database='dev130')
cursorstr = cnx.cursor()
# cursorstr.execute('create table student(id int(25) , first_name varchar(25), last_name varchar(25));')

# # insert value
cursorstr.execute("insert into student values (127,'Neel','Gabani');")
cursorstr.execute("insert into student values (129,'Aditya','Rohila');")
cursorstr.execute("insert into student values (130,'Dev','Patel');")

# delete value 
# cursorstr.execute("delete from student where id=128;")

# # select specific columns
# cursorstr.execute("select id from student;")

# # fetch one 
# cursorstr.execute("select * from student where id=129;")

# update the value 
# cursorstr.execute("update student set last_name='patel' where id=129 ;")

# # display all values
cursorstr.execute("select * from student;")
result=cursorstr.fetchall()
for x in result:
    print(x)
cnx.commit()
