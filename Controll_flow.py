age = int(input("Enter your age : "))

if age >= 0 and age <=24:
    print("You are Student")
elif age >=25 and age <= 58:
    print("You are employee")
else:
    print("You are retired person")

#Ternary Operator 

temp = int(input())

status = "It's Raining" if temp <=10 else "It's not raining"
print(status)