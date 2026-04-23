import pymysql
conn=pymysql.connect(host='localhost', user='user', password='root')
print('connected')
cur=conn.cursor()    
cur.execute('use day2')
cur.execute('show tables')
tables=cur.fetchall()
for x in tables:
    print(x)    