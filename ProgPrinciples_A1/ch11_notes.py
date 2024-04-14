# Ch11 - Inheritance

# Topic 1 - Inheritance 
#   - "IS-A" relationship between two classes
#       - Example: Student is-a Person, Professor is-a Person
#           Dog is-a Animal, Cat is-a Animal, Car is-a Vehicle, Flower is-a Plant
#   - Superclass: base, existing, parent class
#   - Subclass: derived, new, child class
#       - inherite all attributes and methods defined in superclass
#       - can add new attributes and methods
#   - how: class SubclassName(SuperclassName):


# Topic 2 - Overriding and Polymorphism 
#   - Overriding: subclass provides a new implementation to a method inherited from superclass
#       - For example: Student class has its own print_info() to replace the one got from Person
#   - how: define a method of the same name in suclass
#       - to call method in superclass: super().method_name()
    
#   - Polymorphism: (multiple forms)
#       - Python will decide which method to be called based on the type 
#       - to call new methods defined in subclass
#           - isinstance(object, Class): True/False   

# Superclass
class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address 
    
    def print_info(self):
        print(f'Person: {self.name}, {self.age}, {self.address}')
    
    def __str__(self):
        return f'Person: {self.name}, {self.age}, {self.address}'

# Subclass 1 - Student
class Student(Person):
    def __init__(self, name, age, address, learning, grade):
        super().__init__(name, age, address) # call superclass init
        self.learning = learning  # add extra attributes
        self.grade = grade 
    
    def print_info(self): # Overriding 
        print(f'Student: {self.name}, {self.grade}')

    def add_course(self, course): # add extra methods
        self.learning.append(course)
    
    def print_grade(self): # add extra methods
        print(f'Student {self.name} has grade {self.grade}')

    def __str__(self):
        return 'Student' + super().__str__() + f',{self.learning}, {self.grade}'

# Subclass 2 - Professor
class Professor(Person):
    def __init__(self, name, age, address, teaching, salary):
        super().__init__(name, age, address)
        self.teaching = teaching 
        self.salary = salary 
    
    # Overriding
    def print_info(self):
        super().print_info() # call method defined in superclass
        print(f'Professor: {self.teaching}, {self.salary}')

    def print_salary(self): # add extra methods
        print(f'Professor {self.name} has salary {self.salary}')

    # Overriding
    def __str__(self):
        return f'Professor({self.name}, {self.teaching}, {self.salary})'


# polymorphism example
#   - a function takes a list of persons(Person, Student, Professor)
#   - call print_info to each person 
def print_info_persons(persons):
    for person in persons:
        person.print_info()
        if isinstance(person, Student):
            person.print_grade()
        if isinstance(person, Professor):
            person.print_salary()


def test_code():
    p1 = Person('Jack', 18, '100 Main str.')
    p1.print_info() # Person: Jack, 18, 100 Main str.

    s1 = Student('Anna', 17, '123 Queen', ['Python', 'Network', 'Math'], 82.34)
    print(s1.name, s1.age, s1.address) # inherite from Person
    s1.print_info() # inherite from Person
    s1.print_grade() # new method for Student

    p1 = Professor('Alex', 42, '321 King', ['C', 'Java', 'Python'], 1234.56)
    print(p1.name, p1.age, p1.address)
    p1.print_info() 
    p1.print_salary() 

    print(s1)
    print(p1)

    print('#' * 30)
    persons = [Person('Alex', 18, '123 main'),
                Student('Balex', 19, '234 main', [], 66.77),
                Professor('Calex', 39, '345 main', ['JavaScript'], 99999.99)]
    print_info_persons(persons)


# Exercise on page 26: Pet - Dog, Cat, Fox


def main():
    test_code()
main()

# Lab 4

# Out of scope topics:
#   - class attributes/methods VS. instance attributes/methods
#   - multiple inheritance
#   - abstract classes (ABC), interfaces

