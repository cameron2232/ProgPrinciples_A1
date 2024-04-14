
# Lab4 and Quiz4 next two classes

# Review
# - Coin: side_up, __init__, __str__, throw()
# - Circle: radius, __init__, __str__, area()
# - BankAccount: name, type, balance, __init__, __str__, 
#       deposit(), withdraw()
import random
class Coin:
    def __init__(self):
        self.side_up = random.randint(0, 1) # 0-Head, 1-Back
    def throw(self):
        self.side_up = random.randint(0, 1)
    def __str__(self):
        return f'Coin:{'Head' if self.side_up == 0 else 'Back'}'

class Circle:
    def __init__(self, radius=1.0, color='black'):
        self.radius, self.color = radius, color 
    def area(self):
        import math 
        return math.pi * self.radius ** 2 
    def __str__(self):
        return f'Circle:radius={self.radius}, color={self.color}'
    def __repr__(self): # to print a list of objects
        return str(self) + '\n'

class BankAccount:
    def __init__(self, name, atype='checking', balance=100):
        self.name = name 
        self.atype = atype 
        self.balance = balance 
    def deposit(self, amount):
        if amount < 0: print('Amount can not be negative')
        else:
            self.balance += amount 
    def withdraw(self, amount):
        if amount > self.balance or amount < 0:
            print('Invalid amount')
        else:
            self.balance -= amount 
    def __str__(self):
        return f'Bank Account({self.name}, {self.atype}, {self.balance})'
          
def test_review():
    c = Coin()
    for _ in range(10):
        c.throw()
        print(c)

    c1 = Circle() 
    c2 = Circle(2.3, 'red')
    print(c1, c1.area(), c2, c2.area())

    ba = BankAccount('Jack', 'saving', 1000)
    for _ in range(10):
        ba.deposit(random.uniform(0, 200))
        ba.withdraw(random.uniform(200, 500))
        print(ba)
    

# Topic 1 - UML - Unified Modeling Language
#   - class diagram: use a diagram to represent a class
#   - tools: e.g. visual paradigm, umlet
#   - 3 parts: class name, attributes, methods
#       - details: -: private, +:public, name:type 

# Topic 2 - Private attributes, getters and setters 
#   - Note: in python no real private attribute
#   - name attribute with prefixed double underscore: __mark        
#   - getter method (accessor): get value of an attribute
#   - setter method (mutator): update value of an attribute

class Student:
    def __init__(self, id, name, mark):
        self.id = id 
        self.name = name 
        self.__mark = mark # mark is private

    # getters for id, name, mark
    def get_id(self): 
        return self.id 
    
    def get_name(self): 
        return self.name.upper()
    
    def get_mark(self): 
        return self.__mark 

    # setters for id, name, mark 
    # - may add validations
    def set_id(self, id): 
        self.id = id 

    def set_name(self, name): 
        self.name = name 

    def set_mark(self, mark): 
        self.__mark = mark 

def test_student():
    s1 = Student(97531, 'Alex', 67.89)
    print(s1.id, s1.name) # directly accessing
    # print(s1.__mark) # AttributeError: 'Student' object has no attribute '__mark'
    s1.id = 333444 # directly accessing
    s1.name = 'Balex'

    print(s1.get_id(), s1.get_name(), s1.get_mark()) # use getters
    s1.set_id(12345) # use setters
    s1.set_name('Dalex')
    s1.set_mark(77.88)

# Topic 3 - Objects with functions 
#   - functions that accepts objects as arg, returns objects as value

# Example: a function returns a list of random circles
def get_random_circles(num):
    colors = ['red', 'black', 'green', 'blue', 'yellow']
    # return [Circle(random.uniform(10, 100), random.choice(colors)) 
    #         for _ in range(num)]
    # or regular way:
    temp = []
    for _ in range(num):
        c = Circle(random.uniform(10, 100), random.choice(colors))
        temp.append(c)
    return temp

# Example: a function, given a list of circles and a required color
#   return a list of circles containing those circles:
#       - area() is greater than average area
#       - color is required color 
def get_big_colored_circles(circles, required_color):
    average_area = sum([c.area() for c in circles]) / len(circles)
    return [c for c in circles 
            if c.area() > average_area and c.color == required_color]
    # or try to use regular way

def main():
    print(get_random_circles(10))
    circles = get_random_circles(100)
    selected_circles = get_big_colored_circles(circles, 'red')
    print(selected_circles)

    # test_student()
    # test_review()
main()

# >> Break 

# Game Time !!!!
