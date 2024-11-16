x = int(input("Enter any number "))
if (type(x) is int):
    print("True")
else:
    print("False")


y = float(input("Enter any number"))
if (type(y)is not float):
    print("True")
else:
    print("False")


a = int(input("Enter any number"))
b = int(input("Enter any number"))
if (a is b):
    print(a, "and", b, "are the same")
else:
    print(a, "and", b, "are not the same")