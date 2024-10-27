x = int(input("перше число:"))
y = int(input("друге число:"))
c = input("дія:")
ans = 0


if c == "/" and y == 0:
    ans = ("на 0 ділити не можна")
elif c == "/" and y != 0:
    ans = x / y
elif c == "+":
    ans = x+y
elif c == "-":
    ans = x-y
elif c == "*":
    ans = x * y



print(ans)