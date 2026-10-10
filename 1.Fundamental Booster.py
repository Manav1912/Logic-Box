
print("Welcome to the Interactive Personal Data Collector!")
print()

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favoritenumber = int(input("Please enter your favorite number: "))
print()

print("Thank you! Here is the information we collected:")
print()

print("Name:", name, "(Type:", type(name), "Memory Address:", id(name), ")")
print("Age:", age, "(Type:", type(age), "Memory Address:", id(age), ")")
print("Height:", height, "(Type:", type(height), "Memory Address:", id(height), ")")
print("Favorite Number:", favoritenumber, "(Type:", type(favoritenumber), "Memory Address:", id(favoritenumber), ")")
print()

current_year = 2026
birth_year = current_year - age
print("Your birth year is approximately:", birth_year, "(based on your age of", age, ")")
print()

print("Thank you for using the Personal Data Collector. Goodbye!")