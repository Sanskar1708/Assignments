# creat a python program to show how the manager class inherits attributes and methods from both the Person and Employee parent classes, and how we can add attributes behaviours and properties in the manager class. Person class contains common attributes like name and age. Employee class contains attributes like employee ID and salary. Manager class will also contatin some of its own attributes like Department

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee:
    def __init__(self, employeeID, salary):
        self.employeeID = employeeID
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.employeeID}")
        print(f"Salary: {self.salary}")

class Manager(Person, Employee):
    def __init__(self, name, age, employeeID, salary, department):

        Person.__init__(self, name,age)
        Employee.__init__(self, employeeID, salary)

        self.department = department

    def display_info(self):
        print("---Manager Details---")
        Person.display_info(self)
        Employee.display_info(self)
        print(f"Department: {self.department}")
        print("---------------------")

    def conduct_meeting(self):
        print(f"\n[Action] {self.name} is conducting a meeting for the {self.department} department")

#Creating a manager object
mgr1 = Manager("Sairaj", 20, "M1", 6700000000, "IT Department")
mgr1.display_info()
mgr1.conduct_meeting()