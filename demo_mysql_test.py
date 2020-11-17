import mysql.connector
import requests
from fantasytest import sorted_list


mydb = mysql.connector.connect(
  host="localhost",
  user="theting641",
  password="Richboy1!",
  database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "DROP TABLE players"

#mycursor.execute(sql)

#mycursor.execute("CREATE TABLE players (id INT AUTO_INCREMENT PRIMARY KEY, player VARCHAR(255), value DECIMAL(6,3), position VARCHAR(255))")

#sql = "DELETE FROM players WHERE player = 'Christian McCaffrey'"

#mycursor.execute(sql)

#mydb.commit()

#for player in sorted_list:
  #print(player[1])
  #sql = "INSERT INTO players (player, value, position) VALUES (%s, %s, %s)"
  #val = (player[0], player[1], player[2])
  #mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM players")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#mydb.commit()

#print(sorted_list)

