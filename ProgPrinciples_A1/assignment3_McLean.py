import random

def create_db(file_name):
    # TODO 1/7
    # Opens file with provided file_name, trunctating the file if already
    # existing and creates the file if doesn't exist
    # returns true if the file successfully opens, false if an error occurs
    try:
        with open(file_name, 'w'):
            return True
    except Exception:
        return False
    pass

def read_users(file_name):
    # TODO 2/7
    # creates two empty lists to hold name and password
    list_names, list_passwords = [], []
    
    # opens the file in read mode, no editing required
    # reads through each line, seperating the name and password
    # and saves them in respective list. removes \n from the end.
    try:
        with open(file_name, 'r') as file:
            for line in file:
                fields = line.rstrip('\n').split(',')
                list_names.append(fields[0])
                list_passwords.append(fields[1])
        return list_names, list_passwords
                
    #returns two nones if an error occurs
    except Exception:
        return None, None
    pass

def display_users(names, passwords):
    # TODO 3/7
    # checks if there are any users, displays No user found if not
    if len(names) == 0: print('No user found')
    
    # prints out the name and their respective password in a table format
    try:
        if len(names) != 0:
            print('No.  Name                Password\n',
                '----------------------------------')
        for i in range(len(names)):
            print(f'{i+1}    {names[i]: <20}{passwords[i]}')
    
    # returns "No user found" if error is ran into
    except Exception:
        print('No user found')
    pass

def valid_name(name):
    # TODO 4/7

    # verifies that name is at least 3 characters long and returns false if not
    if len(name) < 3:
        return False
    
    # checks every character in the name and verifies they are valid characters
    for i in range(len(name)):
        if((ord(name[i]) >= 65 and ord(name[i]) <= 90) or
           (ord(name[i]) >= 97 and ord(name[i]) <= 122)):
            return True
        else:
            return False           
    pass

def generate_password(name):
    # TODO 5/7

    # adds the first character, and then the numeric length of the name to
    # the start of the password
    generated_password = name[0]
    generated_password += str(len(name))
    
    # generates 3 random characters within a specific range that is added
    # onto the end of the password
    for _ in range(6):
        generated_password += chr(random.randint(33,122))
    return generated_password #returns generated password
    pass

def sign_up(file_name):
    # TODO 6/7
    count = 0
    try:
        while True:
            already_exists = False
            user_name = input('Enter name (\'s\' to Stop): ')
            if user_name == 's': #ends loop if s is entered
                return count
            if valid_name(user_name) == False: # checks for valid name
                print('Name is invalid.')
                continue
            # function checking if the entered name has already been given and 
            # settings already_exists to corresponding boolean
            with open(file_name, 'r') as file:
                for line in file:
                    fields = line.rstrip('\n').split(',')
                    if user_name == fields[0]:
                        print('Name already exists.')
                        already_exists = True
            
            # if name did not exist, generate a password and write the name 
            # and password into the file and increase count
            if already_exists == False:
                user_password = generate_password(user_name)
                print(f'Hello {user_name}, your password is: {user_password}')
                with open(file_name, 'a') as file:
                    file.write(f'{user_name},{user_password}\n')
                    count += 1
    except Exception:
        return -1
    return count

    pass

def change_password(file_name, name, new_password):
    # TODO 7/7
    pass


USER_DB = 'C:/temp/assignment3_McLean.csv'

# == DO NOT MODIFY ANY CODE BELOW THIS LINE ==

def main(): 
    print('Create DB:', create_db(USER_DB)) # Create DB: True
    names, passwords = read_users(USER_DB)
    display_users(names, passwords)  # No user found

    print('Count:', sign_up(USER_DB))
    names, passwords = read_users(USER_DB)
    display_users(names, passwords)

    print('Change first name:',      # Change first name: True
          change_password(USER_DB, names[0], 
                          generate_password(names[0]))) 
    print('Change last name: ',      # Change last name: True
          change_password(USER_DB, names[len(names) - 1], 
                          generate_password(names[len(names) - 1])))
    print('Change dumb name: ',      # Change dumb name: False
          change_password(USER_DB, 'ProfSun', # Username does not exist
                          generate_password('ProfSun'))) 

    names, passwords = read_users(USER_DB)
    display_users(names, passwords)
    
if __name__ == '__main__':
    main()
