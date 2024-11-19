import sqlite3


connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()

#=====CREATE=====
#cur.execute("CREATE TABLE Animals (Name TEXT, Type TEXT)")
#connection.commit()


#====add====

name = input("Name : ")
type = input("Type : ")
cur.execute(f"INSERT INTO Animals (Name, Type) VALUES ('{name, type}');")
connection.commit()
print("Animal added")



connection.close()
