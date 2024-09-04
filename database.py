import mysql.connector
import mysql.connector.connection

def checkUser(account,passwd):
  
    statement="SELECT COUNT(*) FROM Person WHERE username=%s and password = %s"
    values=(account,passwd)
    mycursor.execute(statement,values)
    print("Chay toi ni roi")
    result=mycursor.fetchone()
    if(result==1):
        mycursor.close()
        mydb.close()
        return True
    else :
        mycursor.close()
        mydb.close()
        return False
    
def signupUser(account, passwd):
    

    statement="INSERT INTO VALUES(%s,%s)"
    values=(account,passwd)
    mycursor.execute(statement,values)
    
    
    

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="demo",
    ssl_disabled=True,
)
 
mycursor=mydb.cursor()

    

# mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# statement="INSERT INTO Person(name, age) VALUES (%s,%s) "
# values=('VIET',26)
# mycursor.execute(statement,values)
# mydb.commit()
# mycursor.execute("SELECT * FROM  Person")



