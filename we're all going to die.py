import sqlite3


connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()

#=====CREATE=====
#cur.execute("CREATE TABLE Users (login TEXT, password TEXT)")
#connection.commit()


#====login or register====
Choice = input("login or register : ")
if Choice == 'login':
    login = input("login : ")
    password = input("password : ")
    cur.execute(f"SELECT rowid FROM Users WHERE login= '{login}';")
    connection.commit()
    res = cur.fetchall()
    if res != []:
        pass
    else:
        print('login not registered')
    cur.execute(f"SELECT rowid FROM Users WHERE password= '{password}';")
    connection.commit()
    res = cur.fetchall()
    if res != []:
        print('Successful login')
    else:
        print('incorrect password')


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

#cur.execute(f"SELECT * FROM Animals WHERE Type= 'Ссавець';")
#connection.commit()
#res = cur.fetchall()
#for row in res:
    #print(f"{row[0]} - {row[1]}")


#cur.execute(f"SELECT * FROM Animals")
#connection.commit()
#res = cur.fetchall()
#for row in res:
    #print(f"{row[0]} - {row[1]}")




connection.close()