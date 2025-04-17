number1=float(input("Enter a number :"))
number2=float(input("Enter a number :"))
choice=input("Enter ( + - * /)")
if choice=="+":
    print(number1+number2)
elif choice=="-":
    print(number1-number2)
elif choice=="*":
    print(number1*number2)
elif choice=="/":
    print(number1/number2)
else:
    print("Invalid ")