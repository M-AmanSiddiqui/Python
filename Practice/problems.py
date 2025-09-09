# Q1. Write a Python program to create a class called "Person" with properties for 
# name, age and country. Include a method to display the person's details. Create 
# two instances of the 'Person' class and display their details.
# Ans:1
# class Person:
#     def __init__ (self , name , age , country):
#         self.name = name
#         self.age = age
#         self.country = country
#     def display_info(self):
#         return f'My name is {self.name}. I am {self.age} years old. I live in {self.country}'
# Aman = Person('Aman', 18, 'Pakistan')
# print(Aman.display_info()) # Output: My name is Aman. I am 18 years old. I live in Pakistan
         


#  Q2. Write a Python program to create a class called 'Rectangle' with properties for 
# width and height. Include two methods to calculate rectangle area and perimeter. 
# Create an instance of the 'Rectangle' class and calculate its area and perimeter. 
# Ans:2
# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def cal_area(self):
#         area = self.width *  self.height
#         return area
        
#     def perimeter(self):
#         perimeter = self.width +  self.height
#         return perimeter
    
# Rectangular = Rectangle(9,6)
# print(Rectangular.cal_area()) # Output:54



# Q3. Write a Python program that creates a class called 'Vehicle' with properties for 
# make, model, and year. Include a method to display vehicle details. Create a 
# subclass called 'Car' that inherits from the 'Vehicle' class and includes an 
# additional property for the number of doors. Override the display method to 
# include the number of doors. 
# Ans:3
# class Vehicle:
#     def __init__(self,make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def display_info(self):
#         print(f'the make is {self.make} the model is {self.model} the year is {self.year}')

# class Car(Vehicle):
#      def __init__(self,make, model, year,doors):
#          super().__init__(make, model, year)
#          self.doors = doors
     
#      def display_info(self):
#           super().display_info()
#           print(f'Number of doors {self.doors}')
# my_car = Car("Toyota" , "Corolla" , 2020, 4)
# print(my_car.display_info())  # Output:the make is Toyota the model is Corolla the year is 2020 Number of doors 4



# Q4. Write a Python program that creates a class called "BankAccount" with 
# properties for account number and balance. Include methods to deposit and 
# withdraw money from the account. Create some instances of the "BankAccount" 
# class, deposit some money, and withdraw a portion of it. 
# Ans:4
# class BankAccount:
#     def __init__(self,  acc_number,balance):
#         self.acc_number = acc_number
#         self.balance = balance
#     def Withdraw(self,amount):
#         self.balance -= amount
 
#         print(self.balance)

#     def deposit(self,amount):
#         self.balance += amount

#         print(self.balance)     
# a1 = BankAccount(123 , 1000 )
# a1.deposit(500)  # Output:1500



# Q5. Age Group Categorization 
# Classify a person's age group: child (<13), Teenager (13-19), Adult (20-59), Senior(60+). 
# Ans:5
# age = int(input("Enter our Age:"))
# if age < 13:
#     print("Child")  Output:Child

# elif age < 20:
#     print("Teenager") Output:Teenager
   
# elif age < 60:
#     print("Adult")    Output:Adult

# else:
#     print("Senior")   Output:Senior



# Q6.  Movie ticket are priced based on age: $12 for Adult(18 or over). $8 for children.
#  Everyone gets a 2$ discount on Wednesday.
# Ans:6
# age = int(input("Enter Your age: "))
# day = "Wednesday"
# Price = 12 if age >= 18 else 8
# if day == "Wednesday":
#     Price = Price - 2
# print("Tiket price for you is $",Price) Output:Tiket price for you is $ 6



# Q7.  Grade Calcuator
#     Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-70), D(60-69),F(below 60)
# Ans:7
# score = int(input("Enter Your Marks: "))

# if score >= 101:
#     print("Please Verify Your Grade Again")
#     exit()
# if score >= 90:
#     grade = "A"

# elif  score >= 80:
#      grade = "B"
   
# elif score >= 70:
#     grade = "C"

# elif score >= 60:
#     grade = "D"

# else:
#      grade ="F" 

# print("Grade: ",grade)



# Q8.  Weather Activity Suggestion
#      Suggest an activity based on the weather
#  (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman). 
# Ans:8
  
# weather = "Sunny"

# if weather == "Sunny":
#     activity = "Go for a walk"

# elif weather == "Rainy":
#      activity = "Read a book"

# elif weather == "Snowy":
#      activity = "Build a snowman"


# print(activity)  Output: Go for a walk



# Q9.  Transportation a Mode of Selection
#      Transportation a Mode of Selection base on the distance (e.g., <3 km:Walk, 3-15 km:Bike, >15km: Car)
# Ans:9
# distance = int(input("Enter Your Distance: "))

# if distance < 3:
#     transport = "walk"

# elif distance <=  15:
#     transport = "Bike"

# else:
#     transport = "Car"

# print("AI recommends you the transport of: ",transport)



# Q10.  Coffee Customization
#       Customize a coffee order: "Small", "Medium",  or "Large" with an option for "Extra shot" pf espresso.
# Ans:10

# order_size = "Medium"
# extra_shot = True

# if extra_shot:
#     coffee = order_size + " Coffee with an extra shot"

# else:
#     coffee = order_size + " Coffee"

# print("Order: ",coffee) Output: Order:Medium Coffee with an extra shot



# Q11.  Pssword Strength Checker
#       Check if a password is "Weak", "Medium", or "Strong". 
# Criteria: < 6 chars (Weak), 6-10 chars(Medium), >10 chars(Strong)
# Ans:11

# password = input("Enter Your Password: ")

# if len(password) < 6:
#     strength = "Weak"

# elif len(password) <= 10:
#     strength = "Medium"

# else:
#     strength = "Strong"

# print("Password Strength is: ",strength)



# Q12.  Leap Year Checker
#       Determine if a year is a leap year.(Leap years are divisible by 4, but not by 100 unless also divisible by 400).
# Ans:12
# year = 2024

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(year, " is a leap year") Output: 2024  is a leap yea

# else:
#     print(year , " is Not a leap year")   



# Q13.  Pet Food Recommendation
#       Recommend a type of pet food based on the pet's species age age. 
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
# Ans:13

# dog1 = int(input("Whats Your Dog Age: "))
# cat1 = int(input("Whats Your Cat Age: "))

# if dog1 < 2:
#     dogfood = "Puppy Food"

# elif dog1 >= 2:
#     dogfood = "Adult Food"
    
# if cat1 > 5:
#     catfood= "Senior Cat Food"

# elif cat1 < 5:
#     catfood= "Junior Cat Food"

# print("Your Dog Food is: ",dogfood)
# print("Your Cat Food is: ",catfood)



# Q14.   Counting Positive Numbers
#        Problem: Given a list of numbers, count how many are positive.  
#        numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# Ans:14
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_number_count = 0
# for num in numbers:
#     if num > 0:
#         positive_number_count += 1

# print("Final count of Positive Number is: ",positive_number_count) //Output: 6



# Q15.  Sum of Even Numbers
#       Problem: Calculate the sum of even numbers up to a given number n.
# Ans:15
# n = int(input("Enter Number: "))
# sum_even = 0 
# for i in range (1, n+1):
#     if i%2 == 0:
#         sum_even += 1
# print("Sum of even number is: ," ,sum_even)



# Q16.  Multiplication Table Printer
#       Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
# Ans:16
# number = int(input("Enter Number: "))

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, 'x' , i , '=' , number * i)



# Q17.  Reverse a String
#       Problem: Reverse a string using a loop.
# Ans:17
# input_str = "Python"
# reversed_str = ""

# for char in  input_str:
#     reversed_str = char + reversed_str

# print(reversed_str) Output: nohtyP



# Q18.  Find the First Non-Repeated Character
#       Problem: Given a string, find the first non-repeated character
# Ans:18
# input_str = "teeter"

# for char in input_str:
   
#     if input_str.count(char) == 1:
#         print("Result is :" , char) Output: Result is : r
#         break



#Q19.  Factorial Calculator
#      Problem: Compute the factorial of a number using a while loop.
# Ans:19
# number = int(input("Enter a Number: "))
# factorial = 1

# while number > 0:
#     factorial = factorial * number
#     number = number - 1
#     print("factorial: ",factorial) 



# Q20.   Validate Input
#        Problem: Keep asking the user for input until they enter a number between 1 and 10.
# Ans:20
# while True:
#     number = int(input("Enter value b/w 1 and 10: "))
#     if 1 <= number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid Number")



# Q21.  Prime Number Checker
#       Problem: Check if a number is prime.
# Ans:21
# number = 29
# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break

# print(is_prime)



# Q22. List Uniqueness Checker
#      Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
#      items = ["apple", "banana", "orange", "apple", "mango"]
# Ans:22
# items = ["apple", "banana", "orange", "apple", "mango"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate" , item)
#         break
#     unique_item.add(item)



# Q23.  Exponential Backoff
#       Problem: Implement an exponential backoff strategy that doubles the wait time between retries,
#       starting from 1 second, but stops after 5 retries.
# Ans:23  
# import time

# wait_time = 1
# max_retries = 5
# attemps = 0

# while attemps < max_retries:
#     print("Attempt", attemps  + 1,  "wait_time" , wait_time )
#     time.sleep(wait_time)
#     wait_time *= 2 
#     attemps += 1



# Q24. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.
# Ans:24
# def square(number):
#     return (number ** 2)
# print(square(4)) Output: 16



# Q25. Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum.
# Ans:25
# def add(a , b):
#     return a + b
# print(add(4,6)) Output: 10



# Q26. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
# Ans:26
# def multiply(p1 , p2):
#     return p1 * p2
# print(multiply(5 , 5)) 
# print(multiply(5 , 5)) Output: 25



# Q27. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
# Ans:27
# import math
# def circl(radius):
#      area = math.pi * radius ** 2
#      circumference = 2 * math.pi * radius
#      return area, circumference
# a , c = circl(3)
# print("Area:" , a , "Circumference:",c)  Output: Area: 28.274333882308138 Circumference: 18.84955592153876



# Q28. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
# Ans:28
# def greet(name = "user"):
#     return "Hello, " + name + " !"
# print(greet()) Output: Hello, user !



# Q29. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.
# Ans:29
# cube = lambda x: x ** 3
# print(cube(3)) Output: 27



# Q30. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.
# Ans:30
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1, 2))  Output: 3
# print(sum_all(1, 2, 3, 4 , 5)) Output: 15
# print(sum_all(1, 2, 3, 4 , 5, 6, 7 , 8)) Output: 36



# Q31. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
# Ans:31
# def kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:  {value}")
# kwargs(name="Aman", F_Name="Waqar" ) 
# kwargs(name="Azan", F_Name="Waqar" ) 



# Q32. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.
# Ans:32
# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         yield i
# for num in even_generator(10):
#     print(num)



# Q33. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.
# Ans:33
# def factorial(n):
#     if n == 0: 
#         return 1
#     else:
#         return n * factorial(n - 1)



# Q34. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
# Ans:34
# class Car:
#     def __init__(self,brand, model):
        
#         self.brand = brand
#         self.model = model     

# my_car = Car("Toyota","Corrola")
# print(my_car.brand)
# print(my_car.model)



# Q35. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).
# Ans:35
# class Car:
#     def __init__(self,brand, model):
        
#         self.brand = brand
#         self.model = model

#     def fullName(self):
#         return f"{self.brand} {self.model}"
     

# my_car = Car("Toyota","Corrola")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())



# Q36. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
# Ans:36
# class Car:
#     def __init__(self,brand, model):
        
#         self.brand = brand
#         self.model = model

#     def fullName(self):
#         return f"{self.brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand , model)
#         self.battery_size = battery_size
        
# my_tesla = ElectricCar("Tesla", "Model S" , "85kWh")
# print(my_tesla.fullName(),my_tesla.battery_size)



# Q37. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private,
#  and provide a getter method for it.
# Ans:37
# class Car:
#     def __init__(self,brand, model):
        
#         self.__brand = brand
#         self.model = model
    
#     def get_brand(self):
#         return self.__brand + " !"

#     def fullName(self):
#         return f"{self.__brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand , model)
#         self.battery_size = battery_size
        
# my_tesla = ElectricCar("Tesla", "Model S" , "85kWh")
# print(my_tesla.fullName(),my_tesla.battery_size)
# print(my_tesla.get_brand())


# Q38. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes,
#  but with different behaviors.
# Ans:38
# class Car:
#     def __init__(self,brand, model):
        
#         self.__brand = brand
#         self.model = model
    
#     def get_brand(self):
#         return self.__brand + " !"

#     def fullName(self):
#         return f"{self.__brand} {self.model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand , model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S" , "85kWh")
# safari = Car("Tata","Safari")
# print(my_tesla.fullName(),my_tesla.battery_size)
# print(my_tesla.fuel_type())
# print(safari.fullName())
# print(safari.fuel_type())



# Q39. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.
# Ans:39
# class Car:
#     total_car = 0 
#     def __init__(self,brand, model):
        
#         self.__brand = brand
#         self.model = model
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand + " !"

#     def fullName(self):
#         return f"{self.__brand} {self.model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand , model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S" , "85kWh")
# safari = Car("Tata","Safari")
# print(my_tesla.fullName(),my_tesla.battery_size)
# print(my_tesla.fuel_type())
# print(safari.fullName())
# print(safari.fuel_type())
# print(Car.total_car)



# Q40. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.
# Ans:40
# class Car:
#     total_car = 0 
#     def __init__(self,brand, model):
        
#         self.__brand = brand
#         self.model = model
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand + " !"

#     def fullName(self):
#         return f"{self.__brand} {self.model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod
#     def general_description():
#         return "Cars are means of transport"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand , model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S" , "85kWh")
# safari = Car("Tata","Safari")
# print(my_tesla.fullName(),my_tesla.battery_size)
# print(my_tesla.fuel_type())
# print(safari.fullName())
# print(safari.fuel_type())
# print(Car.total_car)

# print(Car.general_description())



# Q41. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.
# Ans:41
# class Car:
#     total_car = 0 
#     def __init__(self,brand, model):
        
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand + " !"

#     def fullName(self):
#         return f"{self.__brand} {self.__model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod
#     def general_description():
#         return "Cars are means of transport"

#     @property
#     def model(self):
#         return self.__model

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand , model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S" , "85kWh")
# safari = Car("Tata","Safari")
# print(my_tesla.fullName(),my_tesla.battery_size)
# print(my_tesla.fuel_type())
# print(safari.fullName())
# print(safari.fuel_type())
# print(Car.total_car)
# print(Car.general_description())
# print(my_tesla.model)



# Q42. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
# Ans:42
# class Car:
#     total_car = 0 
#     def __init__(self,brand, model):
        
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand + " !"

#     def fullName(self):
#         return f"{self.__brand} {self.__model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod
#     def general_description():
#         return "Cars are means of transport"

#     @property
#     def model(self):
#         return self.__model

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand , model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S" , "85kWh")
# safari = Car("Tata","Safari")
# print(my_tesla.fullName(),my_tesla.battery_size)
# print(my_tesla.fuel_type())
# print(safari.fullName())
# print(safari.fuel_type())
# print(Car.total_car)
# print(Car.general_description())
# print(my_tesla.model)
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))




# Q43. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both,
#  demonstrating multiple inheritance.
# Ans:43
# class Battery:
#     def battery_info(self):
#         return "This is Battery"

# class Engine:
#     def engine_info(self):
#         return "This is Engine"
    
# class Electric_Car(Battery,Engine):
#      def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# my_tesla = Electric_Car("Tesla", "Model S")
# print(my_tesla.engine_info())
# print(my_tesla.battery_info())


# Q44: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.
# Ans:44
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)
# example_function(2)
    


# Q45: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.
# Ans:45
# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k}={v}" for  k, v in kwargs.items())
#         print(f"calling: {func.__name__} with args {args_value} aand kwargs {kwargs_value}")
#         return func(*args, **kwargs)
#     return wrapper

# @debug
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}")

# greet("chai" , greeting="hii")



# Q46: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, 
# so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
# Ans:46
# import time

# def cache(func):
#     cache_value = {}
#     print(cache_value)
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args] = result
#         return result
#     return wrapper
# @cache
# def long_runing_function(a, b):
#     time.sleep(4)
#     return a + b

# print(long_runing_function(2,3))
# print(long_runing_function(2,3))
# print(long_runing_function(4,3))
# print(long_runing_function(5,3))