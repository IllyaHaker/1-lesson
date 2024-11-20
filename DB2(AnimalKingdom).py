import sqlite3


connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()

#=====CREATE=====
#cur.execute("CREATE TABLE Animals (Name TEXT, Type TEXT)")
#connection.commit()


#====add====

# name = input("Name : ")
# type = input("Type : ")
# cur.execute(f"INSERT INTO Animals (Name, Type) VALUES ('{name}', '{type}');")
# connection.commit()
# print("Animal added")

#========UPDATE======
# name_s = input("OLD Name : ")
# name_n = input("New Name : ")
# cur.execute(f"SELECT rowid FROM Animals WHERE Name= '{name_s}';")
# connection.commit()
# res = cur.fetchall()
# if res !=[]:
#     id = int(res[0][0])
#     cur.execute(f"UPDATE Animals SET Name='{name_n}' WHERE rowid={id} ")
#     connection.commit()

#========SELECT======

cur.execute(f"SELECT * FROM Animals WHERE Type= 'Ссавець';")
connection.commit()
res = cur.fetchall()
for row in res:
    print(f"{row[0]} - {row[1]}")


cur.execute(f"SELECT * FROM Animals")
connection.commit()
res = cur.fetchall()
for row in res:
    print(f"{row[0]} - {row[1]}")




connection.close()
