# OOP - 1/3 (ch10a)

# +. Topic 1 - Procedural programming VS. Object-oriented programming
# - procedural programming (structured)
#   - data is separated from operations
#   - focus on writing functions (how)
# - object-oriented programming
#   - encapsulation: data and operations are put togeter
#     - data safe, reusable
#   - focus on writing classes, creating objects (what)

# Example: calculate the total areas and perimeters of two rectangles

# Ver1: Procedural programming
# - two functions: area(width, height), perimeter(width, height)
# - an app function to call the two functions
def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

def procedural_app():
    w1, h1 = 1.2, 2.3
    w2, h2 = 3.4, 4.5
    a1 = area(w1, h1)
    a2 = area(w2, h2)
    p1 = perimeter(w1, h1)
    p2 = perimeter(w2, h2)
    print(f'Total area: {a1 + a2}, Total perimeter: {p1 + p2}')

# Ver2: Object-oriented programming
# - 1. define class; 2. create objects
class Rectangle:
    def __init__(self, width, height):
        self.width = width # self.width: attribute
        self.height = height 
    def area(self):
        return self.width * self.height 
    def perimeter(self):
        return 2 * (self.width + self.height)
    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'

def oop_app():
    r1 = Rectangle(1.2, 2.3) # create an object
    r2 = Rectangle(3.4, 4.5)
    # no __str__:
    # <__main__.Rectangle object at 0x0000017EDA34BB00> 
    # <__main__.Rectangle object at 0x0000017EDA34BB90>
    # after adding __str__:
    # Rectangle(1.2, 2.3) Rectangle(3.4, 4.5)
    print(r1, r2)
    
    a1 = r1.area()
    a2 = r2.area()
    p1 = r1.perimeter()
    p2 = r2.perimeter()
    print(f'Total area: {a1 + a2}, Total perimeter: {p1 + p2}')

# +. Topic 2: classes and objects
#  - class: represent entities (noun), blueprint, type  
#    - define: class MyClassName: 
#       - naming: convention is CamelCase  
#       - attributes: data, state, property, variable
#       - methods: function, action, activity, operation 
#           - first param: self, reference to current object operating on
#               - 'this' in Java
#           - __init__: initialer method, initialize attributes
#           - many other methods: depending on app   
#           - __str__: return a string representation of an object
#               - called automatically when needing a string
#  - object: specific/concreate entites created from class, instance, value
#   - create: obj_name = ClassName(arguments)    
#   - access data: obj_name.attribute (not recommended)
#   - call method: obj_name.method(arguments) 
    
# Example: class Dice 
# - data: point 
# - method: roll(), __init()__, __str__()
class Dice:
    def __init__(self, point=1):
        self.point = point 
    
    def roll(self):
        import random 
        self.point = random.randint(1, 6)
    
    def __str__(self):
        return f'Dice:{self.point}'

def test_dice():
    d1 = Dice()  # testing __init__
    d2 = Dice(3) 
    print(d1, d2) # testing __str__
    for _ in range(10):
        d1.roll() 
        print(d1)

# Example: class Counter
# - data: number, limit, alarm 
# - methods: increment, set_alarm, set_limit, reset 
class Counter:
    def __init__(self):
        self.number = 0
        self.limit = 100
        self.alarm = False 

    def increment(self):
        self.number += 1
        if self.alarm and self.number >= self.limit:
            print('ALARM!!!!')

    def set_alarm(self, alarm): # True - On, False- Off
        self.alarm = alarm
        if self.alarm and self.number >= self.limit:
            print('ALARM!!!!')

    def set_limit(self, limit):
        self.limit = limit 
        if self.alarm and self.number >= self.limit:
            print('ALARM!!!!')

    def reset(self):
        self.number = 0
        self.limit = 100
        self.alarm = False 

    def __str__(self):
        return f'Counter({self.number}, {self.limit}, {self.alarm})'

def test_counter():
    c1 = Counter()
    print(c1)
    c1.set_limit(20)
    c1.set_alarm(True) 
    for _ in range(25):
        c1.increment()
        print(c1)

# Exercises: write classes
# - Coin: side_up, __init__, __str__, throw()
# - Circle: radius, __init__, __str__, area()
# - BankAccount: name, type, balance, __init__, __str__, 
#       deposit(), withdraw()
# - Student: attributes and methods you decide
        
def main():
    test_counter()
    # test_dice()
    # procedural_app()
    # oop_app()

main()
