
def menu():
    print("\n--------- SIMPLE CALCULATOR -----------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Division")
    print("5. Remainder")
    print("6. Sqaure")
    print("7. Cube")
    print("8. Exit")

while True :
    menu()
    choice = int(input("Choose a option : "))
    if choice == 1:
        a = float(input("Enter First no. : "))
        b = float(input("Enter Second no. : "))
        print("Sum = ",a+b)
    elif choice == 2:
        a = float(input("Enter First no. : "))
        b = float(input("Enter Second no. : "))
        print("Subtraction = ",a-b)
    elif choice == 3:
        a = float(input("Enter First no. : "))
        b = float(input("Enter Second no. : "))
        print("Product = ",a*b)
    elif choice == 4:
        a = float(input("Enter First no. : "))
        b = float(input("Enter Second no. : "))
        if(b==0):
            print("Enter Valid, Number")
        else :
            print("Division = ",a/b)
    elif choice == 5:
        a = float(input("Enter First no. : "))
        b = float(input("Enter Second no. : "))
        print("Remainder = ",a%b)
    elif choice == 6:
        a = float(input("Enter no. : "))
        print("Sqaure = ",a**2)
    elif choice == 7:
        a = float(input("Enter no. : "))
        print("Cube = ",a**3)
    elif choice == 8:
        break
    else :
        print("Invalid option, Please choose a valid option")