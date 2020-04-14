import pymysql as ps
from pymysql import Error
import pymysql.cursors
import pymysql

url = '127.0.0.1'
port = 3306
user = 'root'
passwd = 'Root@123'
db = 'taobao'

import pymysql

# 打开数据库连接
db = pymysql.connect(url, user, passwd, db)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()

# print("Database version : %s " % data)
# cursor.execute("drop table IF EXISTS  EMPLOYEE")

# sql = '''
# CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )
# '''
# sql = '''
# INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)
# '''

sql = """
select * from EMPLOYEE
"""
try:
    # 执行数据库操作
    cursor.execute(sql)
    #该方法获取下一个查询结果集。结果集是一个对象
    results = cursor.fetchall()
    #提交数据
    #db.commit()
    print(results)
except:
    #回滚数据
    db.rollback()

# 关闭数据库连接
db.close()


