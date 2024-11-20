import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

#=====CREATE=====
#cur.execute("CREATE TABLE users (login TEXT)")
#connection.commit()


#name = input("Login : ")
#cur.execute(f"INSERT INTO users (login) VALUES ('{name}');")
#connection.commit()
#("Login added")
#connection.close()

#========SELECT==========
#cur.execute(f"SELECT * FROM users")
#cur.execute(f"SELECT * FROM users WHERE login= 'Kyril'")
#connection.commit()
#res = cur.fetchall()
#print(res)

#========UPDATE======
# name_s = input("OLD Login : ")
# name_n = input("New Login : ")
# cur.execute(f"SELECT rowid FROM users WHERE login= '{name_s}';")
# connection.commit()
# res = cur.fetchall()
# if res !=[]:
#     id = int(res[0][0])
#     cur.execute(f"UPDATE users SET login='{name_n}' WHERE rowid={id} ")
#     connection.commit()

#======DELETE======
# cur.execute(f"DELETE FROM users WHERE rowid=3;")
# connection.commit()

connection.close()