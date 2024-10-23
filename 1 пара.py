x = int(input("перше число:"))
y = int(input("друге число:"))
c = input("дія:")
ans = 0

if c == "/" and y == 0:
    print("на 0 ділити не можна")

if c == "/":
    ans = x / y

if c == "+":
    ans = x+y
if c == "-" and y == 0:
    ans = x-y
if c == "*" and y == 0:
    ans = x * y
print(ans)