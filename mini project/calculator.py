# This is a CLI calculator 

def add(a,b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    if b == 0:
        print("Division by 0 is not allowed")
    return a/b
while True:
    print("\n Menu")
    print("1.Addition \n2.Subtarction \n3.Mutiplication \n4.Division \n5.Exit")
    
    
    option=input("Please enter your choice: ").strip()
    
    if option == "5":
        print("Bye !!")
        break
    
    num1=float(input("Enter the first number:").strip())
    num2=float(input("Enter the second number:").strip())
          
    if option == "1":
        result = add(num1, num2)
        print("Addition is :", result)
    
    elif option == "2":
        result = sub(num1, num2)
        print("Subtraction is : ", result)
        
    elif option == "3":
        result = mul(num1, num2)
        print("Multiplication is :", result)
        
    elif option == "4":
        result = div(num1, num2)
        print("Division is :", result)
        
    else:
        print("Invalid option!!")