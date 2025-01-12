#Basic calculator
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
operator= input("Enter your operator: ")
#If block of code:
if operator=="+":
    result=num1 +num2
    print("The result of the sum of the two numbers is: ", result)
elif operator=="-":
    result=num1 -num2
    print("The result of the difference between the two numbers is: ", result)
elif operator=="*":
    result=num1 *num2
    print("The result of the multiplication of the two numbers is: ", result)
elif operator=="/":
    result=num1 /num2
    print("The result of the division of the two numbers is: ", result)
else:
    print("Invalid operator")
    
    

