import sqlite3

list = ["Samsung","Apple", "Huawei", "Nokia", "Lenovo", "Dell", "HP", "LG", "Canon", "Nikon", "Sony"]

list = sorted(list)

connection = sqlite3.connect("Electronics.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE if not exists electronics(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL)")

for i in range(len(list)):
  cursor.execute("insert into electronics (name) values (?)",[list[i]])
  print("added ", list[i])


connection.commit()
connection.close()