a = 10
b = 3

print(f"Addition: {a+b}")
print(f"Substraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
print(f"Power: {a**b}")
print(f"Division1: {a//b}")

x = int(input("enter the value of X : "))
y = int(input("enter the value of Y : "))

#print(x ** y)

x, y = y,x
print(f"value of X:{x}", f"value of Y:{y}")