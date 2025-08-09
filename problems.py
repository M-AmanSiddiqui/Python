# Q1. Write a Python program to create a class called "Person" with properties for 
# name, age and country. Include a method to display the person's details. Create 
# two instances of the 'Person' class and display their details.

# Ans:1
class Person:
    def __init__ (self , name , age , country):
        self.name = name
        self.age = age
        self.country = country
    def display_info(self):
        return f'My name is {self.name}. I am {self.age} years old. I live in {self.country}'
Aman = Person('Aman', 18, 'Pakistan')
print(Aman.display_info()) # Output: My name is Aman. I am 18 years old. I live in Pakistan
         

#  Q2. Write a Python program to create a class called 'Rectangle' with properties for 
# width and height. Include two methods to calculate rectangle area and perimeter. 
# Create an instance of the 'Rectangle' class and calculate its area and perimeter. 

# Ans:2

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def cal_area(self):
        area = self.width *  self.height
        return area
        
    def perimeter(self):
        perimeter = self.width +  self.height
        return perimeter
    
Rectangular = Rectangle(9,6)
print(Rectangular.cal_area()) # Output:54


# Q3. Write a Python program that creates a class called 'Vehicle' with properties for 
# make, model, and year. Include a method to display vehicle details. Create a 
# subclass called 'Car' that inherits from the 'Vehicle' class and includes an 
# additional property for the number of doors. Override the display method to 
# include the number of doors. 

# Ans:3

class Vehicle:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f'the make is {self.make} the model is {self.model} the year is {self.year}')

class Car(Vehicle):
     def __init__(self,make, model, year,doors):
         super().__init__(make, model, year)
         self.doors = doors
     
     def display_info(self):
          super().display_info()
          print(f'Number of doors {self.doors}')
my_car = Car("Toyota" , "Corolla" , 2020, 4)
print(my_car.display_info())  # Output:the make is Toyota the model is Corolla the year is 2020 Number of doors 4


# Q4. Write a Python program that creates a class called "BankAccount" with 
# properties for account number and balance. Include methods to deposit and 
# withdraw money from the account. Create some instances of the "BankAccount" 
# class, deposit some money, and withdraw a portion of it. 

# Ans:4

class BankAccount:
    def __init__(self,  acc_number,balance):
        self.acc_number = acc_number
        self.balance = balance
    def Withdraw(self,amount):
        self.balance -= amount
 
        print(self.balance)

    def deposit(self,amount):
        self.balance += amount

        print(self.balance)     
a1 = BankAccount(123 , 1000 )
a1.deposit(500)  # Output:1500



# Q5. Write a Python program that creates a class called 'Shape' with a method to 
# calculate the area. Create two subclasses, 'Circle' and 'Triangle', that inherit from 
# the 'Shape' class and override the area calculation method. Create an instance of 
# the 'Circle' class and calculate its area. Similarly, do the same for the 'Triangle' 
# class. 
    
# Ans:5



        