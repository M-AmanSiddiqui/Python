# 1) Age Group Categorization

# user = int(input("Enter Your Age: "))

# if user < 13:
#     print("Child")
# elif user < 20:
#     print("Teenager")
# elif user < 50:
#     print("Adult")
# else:
#     print("Senior")


# 2) Movie Ticket Pricing

# age = int(input("Enter Your Age: "))
# day = input("Enter Day: ")
# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     price = price - 2
# print(price)



# 3) Grade CalCulator

# marks = int(input("Enter Your Marks: "))

# if marks >= 101:
#     print("Please verify your grade again")
#     exit()
# if marks >= 90:
#     print("Your Grade is A")
# elif marks >= 80:
#     print("Your Grade is B")    
# elif marks >= 70:
#     print("Your Grade is C")
# elif marks >= 60:
#     print("Your Grade is D")
# else:
#     print("Fail")


# 4) Fruit Ripeness Checker

# fruit = "Banana"
# color = input("Enter Color: ")

# if fruit == "Banana":
#     if color == "Green":
#         print("Unripe")
#     elif color == "Yellow":
#         print("Ripe")
#     elif color == "Brown":
#         print("OverRipe")

    
# 5) Weather Activity Suggestion

# weather = input("Enter Weather: ")

# if weather == "Sunny":
#     print("Go for a walk")
# elif weather == "Snowy":
#     print("Build a snowman")

# 6) Transportation Mode Selection

# distance = int(input("Enter km: "))

# if distance < 3:
#     print("By Walk")
# elif distance < 15:
#     print("Bike")
# elif distance > 15:
#     print("Car")

# 7) Coffee Customization

# order_size = "Medium" 
# extra_shot = True

# if extra_shot:
#     coffee = order_size + " coffee with an extra shot"
# else:
#     coffee = order_size + " coffee"
# print("Order: ", coffee)

# 8) Password Checker

# password = input("Enter Your Password: ")

# if len(password) < 6:
#     print("Weak")
# elif len(password) <= 10:
#     print("Medium")
# else:
#     print("Strong")

# 9) Leap Your Checker 

# year = 2023

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year", year)
# else:
#     print("Not Leap Year",year)

# 10) Pet Food Recommendation

pet = input("Enter Your Pet: ")
age = int(input("Enter Your Pet Age: "))

if pet == "Dog" and age < 2:
    print("Puppy Food")
elif pet == "Cat" and age > 5:
    print("Senior Cat Food")
else:
    print("Regular Food")
