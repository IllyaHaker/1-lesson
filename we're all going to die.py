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

    cur.execute(f"SELECT rowid FROM Users WHERE login= '{login}' and password= '{password}';")
    connection.commit()
    res = cur.fetchall()
    if res != []:
        print('Successful login')

    else:
        print('incorrect login or password')


if Choice == 'register':
    login = input("login : ")
    cur.execute(f"SELECT rowid FROM Users WHERE login= '{login}';")
    connection.commit()
    res = cur.fetchall()
    if res != []:
        print('this login already exists')
    if res == []:
        password = input("password : ")
        cur.execute(f"INSERT INTO Users (login, password) VALUES ('{login}', '{password}');")
        connection.commit()
        print("User added")










connection.close()