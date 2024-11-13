


# print("File open")
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     c = a / b
#     print("Data save")
#     print(c)
# except:
#     print("Error")
# finally:
#     print("file closing")
#     print("Kapibara")
#
# print("'_'")

def checker(var):
    if type(var) != str:
        raise TypeError(f"var {type(var)}is not string")
    return var
try:

    a = 10
    print(checker(a))
except(TypeError) as ex:
    print(ex)
