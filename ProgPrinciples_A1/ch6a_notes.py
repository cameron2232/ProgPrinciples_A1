# Assignment 3 (10%, ch6-8) posted

# Plan on 7B
# - ch6-files (2)
# - ch7-lists (3)
# - ch8-strings (1)
# - ch10-11 -OOP (3)
# - ch9-dictionaries (1)
# - ch12-recursion (1)
# - 2 assignments (10% each), 2 quizzes (2.5% each), 2 bonus labs (0.5%)
# - final exam (35%)

# ==========================================================

# ch6a - Files - 1/2

# Topic 1 - Files in general
# - what and why: store data in storage permanently
#   - programs, videos, music, images, documents, ...
# - two types:
#   - text files: .txt, .py, for human to read, contents are strings (123), encoding/decoding
#   - binary files: .docx, .exe, .jpg, .mp4, for machine(tools) to read, raw data, no encoding/decoding
# - two accessing modes:
#   - sequential-accessing: start from the beginning of the file
#   - random-accessing: directly jump to the place of the data
# - File organization
#   - In hierarchical structure (tree structure)
#       - root - branches - leaves
#   - two types of path: absolute or relative path 

# Topic 2 - File operations
# - two operations: reading and writing
#   - read: get data from file in storage to variables in program
#   - write: move data from variables in program to files in storage
#   - file object: a variable in program to associate with the file
# - how: 1) open/create; 2) read/write; 3) close
#  1. open/create: file_object = open('filename', mode)
#   - filename: absolute or relative
#   - mode: 'w', 'a', 'r' - write, append, read 
#   - if file doesn't exist:
#       - 'w', 'a': create the file
#       - 'r': error 
#   - if file exists:
#       - 'w': all content is cleaned up/overwritten/truncated
#       - 'a': new data appended to end of existing content
#       - 'r': can read 

#  2. read/write 
#   2.1 write: file_object.write(string)
#       - convert values to string: str(...)
#       - write a new line: '\n'

#   2.2 read 
#   - content = file_object.read() # read entire file 
#   - line = file_object.readline() # read one line
#       - remove new line: string.rstrip('\n')

#  3. close: file_object.close()
#    - release resources, be sure data in buffer will be written
#
import random

def file_tester():
    # 1. open/create 
    file = open('example.txt', 'w') 

    # 2. write: 5 'hello world', 5 random numbers 
    for _ in range(5):
        file.write('hello world\n')

    for _ in range(5):
        file.write(str(random.randint(0, 100)) + '\n') 

    # 3. close 
    file.close()

    # 1. open for reading
    file = open('example.txt', 'r')
    # 2. read: read() readline()
    # content = file.read() # read entire file
    # print(content)
    for _ in range(5):
        # 'hello world\n'
        line = file.readline().rstrip('\n') # rstrip to remove '\n'        
        print(line)
    
    for _ in range(5):
        # '34\n'
        line = file.readline()
        print(int(line)) # int(...) will remove the '\n'

    # 3. close 
    file.close()

# Topic 3 - with, loop, CSV 
# - with: context manager, automatically close the file
#     with open(filename, mode) as file_object:
#         statements    
# - loop: read from file line by line, processing
#   - for line in file_object:
#   - while line != '': empty string means the end of file
# - CSV: comma separated values - standard text file format
#   - each row is for one record/item, fields in row separated by comma
#       product name,produced year,price 
#       phone,2022,13424.234
#       car,2003,355534.324
#       ....            
    
# Example: read product name, year, price until 'stop', 
#   write data into a file in CSV format 
#   read from the file, print all data, average price
    
def product_file():
    # writing
    with open('products.csv', 'w') as f:
        name = input('Product name: ')
        while name != 'stop':
            year = int(input('Product year: '))
            price = float(input('Product price: '))
            f.write(f'{name},{year},{price}\n')
            name = input('Product name: ')

    # reading
    with open('products.csv', 'r') as f: 
        total, count = 0.0, 0

         #using for loop to go over the file line by line
        for line in f:
             # phone,2022,235235.23\n -> name, year, price
             fields = line.rstrip('\n').split(',') # a list
             name = fields[0]
             year = int(fields[1])
             price = float(fields[2]) 
             print(f'{name:15}{year:8}{price:10}') #:width
             total += price 
             count += 1 

        # using while loop to do the same
        line = f.readline()
        while line != '': # check end of file 
            fields = line.rstrip('\n').split(',') # a list
            name = fields[0]
            year = int(fields[1])
            price = float(fields[2]) 
            print(f'{name:15}{year:8}{price:10}') #:width
            total += price 
            count += 1             
            line = f.readline() # read next line

        if count > 0:
            print(f'Average: {total / count:.2f}')

def main():
    # file_tester()
    product_file()

main()

