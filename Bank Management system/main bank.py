
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='welcome',database='bank')
cur = conn.cursor()
print('                                                                                                                 WELCOME TO GSS BANK                                                                             ')

print('1. REGISTER')
print(" ------------------------------------------------------------")
print('2. LOGIN')
print(" ------------------------------------------------------------")


n=int(input('Enter your Choice : '))
print()

if n== 1:
     name=input('Enter a Username : ')
     print(" ------------------------------------------------------------")
     passwd=int(input('Enter a 4 DIGIT Password : '))
     print(" ------------------------------------------------------------")
     V_SQLInsert="INSERT  INTO user_table (passwrd,username) values (" +  str (passwd) + ",' " + name + " ') "
     cur.execute(V_SQLInsert)
     conn.commit()
     print()
     print('USER created succesfully')
     import MENU

if  n==2 :
     print("You've selected Option2 (Login)")
     print(" ------------------------------------------------------------")
     name=input('Enter your Username : ')
     print(" ------------------------------------------------------------")
     passwd=int(input('Enter your 4 DIGIT Password : '))
     print(" ------------------------------------------------------------")
     V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and username=  ' " +name+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchone() is  None:
          print()
          print('Invalid Username or Password')
     else:
          print()
          import MENU
     
     
