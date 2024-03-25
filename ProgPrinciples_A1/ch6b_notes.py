# Review
# - Files in general 
# - File operations
#   - with open(filename, mode) as file:
#   - writing: file.write(string)
#   - reading: read(), readline()
#       - for line in file:
#       - while line != '':
#   - close()
# - CSV: comma separated values 
#   - row: record 
#   - value: field/attribute 

# File - 2/2

# Topic 1 - File processing 
# - CRUD: create/add new, read/retrieve, update, delete
# - Example: Employee Management System 

def parse_line(line):
    # given 'name,age,salary\n', return name, age, salary 
    fields = line.rstrip('\n').split(',')
    return fields[0], int(fields[1]), float(fields[2])

def add_new(filename):
    # repeatly reading employee data, write to the file
    with open(filename, 'a') as file:
        # can read three data one by one
        line = input('Enter name,age,salary (s-Stop): ')
        while line != 's':
            # if reading 3 data: file.write(f'{name},{age},{salary}\n')
            file.write(line + '\n')
            line = input('Enter name,age,salary (s-Stop): ') 

def print_all(filename):
    # read all records, print in a table
    with open(filename, 'r') as file:
        print(f'{"Name":15}{"Age":10}{"Salary":12}') # :width
        count = 0 
        for line in file:
            name, age, salary = parse_line(line)
            print(f'{name:15}{age:<10}{salary:<12}') # number aligned to left
            count += 1 
        if count == 0: print('No employee found in file')
        else: print(f'We have {count} employees')

def search(filename):
    # read search key (name), look for it in file, print info if found
    key = input('Enter name to search: ')
    with open(filename, 'r') as file:
        for line in file:
            name, age, salary = parse_line(line)
            if name == key: 
                print('Found the employee: ')
                print(f'Name: {name}\nAge: {age}\nSalary: {salary}') 
                break 
        else: 
            print(f'No employe found of name {key}')

def update(filename):
    # read name to find the employee, read new name, new age, new salary
    key = input('Enter name to update: ')
    with open(filename, 'r') as orgi, open('temp.csv', 'w') as dest:
        updated = False
        for line in orgi: 
            name, age, salary = parse_line(line) 
            if name == key: 
                print(f'Found it: {name}, {age}, {salary}')
                name = input('New name: ')
                age = int(input('New age: '))
                salary = float(input('New salary: '))
                updated = True 
            dest.write(f'{name},{age},{salary}\n')
    # if updated, delete original, rename temp to original
    import os 
    if not updated:
        print('Can not find the name')
        os.remove('temp.csv')
    else:
        os.remove('employees.csv')
        os.rename('temp.csv', 'employees.csv')

def delete(filename):
    # read name to delete, if found, remove it
    key = input('Enter name to delete: ')
    with open(filename, 'r') as orgi, open('temp.csv', 'w') as dest:
        updated = False
        for line in orgi: 
            name, age, salary = parse_line(line) 
            if name == key: 
                print(f'Found it: {name}, {age}, {salary}')
                updated = True 
            else:                
                dest.write(f'{name},{age},{salary}\n')
    # if updated, delete original, rename temp to original
    import os 
    if not updated:
        print('Can not find the name')
        os.remove('temp.csv')
    else:
        os.remove('employees.csv')
        os.rename('temp.csv', 'employees.csv')

def emsys():
    # print menu, read user's choice
    filename = 'employees.csv'
    with open(filename, 'a') as f:
        pass 
    while True:
        print('1-add new\n2-print all\n3-search\n' +
              '4-update\n5-delete\n0-exit')
        choice = int(input('Your choice (0-5): '))
        if choice == 1: add_new(filename)
        elif choice == 2: print_all(filename)
        elif choice == 3: search(filename)
        elif choice == 4: update(filename)
        elif choice == 5: delete(filename)
        elif choice == 0: break 
        else: print('Invalid choice')

# Topic 2 - Exception handling
# - what: run-time errors (an exception is raised or thrown)
# - why: program has crash if not handled
# - Examples:
#   1. try to read from a file that doesn't exist
#   2. try to write to a file that is read-only
#   3. try to read a number, user's input is 'abcxyz'
# - how: general form 
#   - if exception: try-except-finally 
#   - if no exception: try-else-finally        
#       try:
#           normal statements # may raise errors
#       except ExceptionType1 as err:
#           statements # handler 
#       except ExceptionType2 as err:
#           statements # handler
#       ...
#       except Exception as err: 
#           statements 
#       else: 
#           statements to be run when no exception 
#       finally:
#           statements to be run in any case                                             

def exception_handling():
    # 1. open a file for reading
    try:
        with open('a_file_that_not_exist.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError as err: 
        print('Got an error: ', err)

    # 2. try to create a file in a folder that doesn't exist 
    #   - homework: try to write to a read-only file 
    try:
        with open('C:/honghahongha/dumb.txt', 'w') as file: 
            print('File created')
    except Exception as err:
        print(err)

    # 3. try to read number from the user
    while True:        
        try:         
            age = int(input('Enter your age: '))
            print('Oh you are so young!')
            break
        except ValueError as err:
            print(err)

# exercises on page 37 (file processing), 43, 51 and 52 (exceptions)

def main():
    # emsys() 
    exception_handling()

main()
