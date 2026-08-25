print("Welcome to the Pattern Generator and Number Analzer!")
print()
print("Select an Option:")
print("1.Right-angled Triangle")
print("2.Pyramid")
print("3.Left-angles Triangle")
print("4.Analyze a Range of Numbers")

choice = input("Enter your choice: ")

# 1.
if choice == "1":
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Invalid row count! Please enter a positive number.")
            
       
        print()

        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()
# 2.
elif choice =="2":
    rows = int(input("Enter the number of rows for the pattern: "))
    if rows <=0:
      
       print()
       
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
       
        for j in range(2 * i - 1):
                       print("*", end="")
       
        print()
        
# 3
elif choice == "3":
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Invalid row count!")

        for i in range(1, rows + 1):
            print(" " * (rows - i), end="")

            for j in range(i):
                print("*", end="")

            print()

# 4
elif choice == "4":
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))

        if end < start:
            print("End number must be greater than start number!")
            

        total = 0

        print("Number Analysis:")

        for number in range(start, end + 1):

            if number % 2 == 0:
                print(number, "is Even")
            else:
                print(number, "is Odd")

            total = total + number

        print("Sum of all numbers:", total)
            
# 5
elif choice == "5":
        print("Thank you for using the program!")
                                            

else:
        print("Invalid choice! Please try again.")