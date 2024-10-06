import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='welcome',database='bank')
if conn.is_connected( ):
    print('Connected Successfully')

cur = conn.cursor()
cur.execute('create table customer_details(acc_no int primary key,acct_name varchar(30),phone_no int(25) check(phone_no>11),adress varchar(25),cr_amt float)')
