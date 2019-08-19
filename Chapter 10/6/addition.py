num1 = input("Enter a number: ")
try:
    num1 = int(num1)
except ValueError:
    print("Sorry you did not enter a number.")
else:
    num2 = input("Enter a second number: ")
    try:
        num2 = int(num2)
    except ValueError:
        print("Sorry you did not enter a number.")
    else:
        print(num1 + num2)
        
        
