import random
from tempfile import TemporaryDirectory 

def create_db(file_name):
    # TODO 1/7
    try:
        with open(file_name, 'w'):
            return True
    except Exception:
        return False
    pass

def read_users(file_name):
    # TODO 2/7
    list_names, list_passwords = [], []
    
    try:
        with open(file_name, 'r') as file:
            for line in file:
                fields = line.rstrip('\n').split(',')
                list_names.append(fields[0])
                list_passwords.append(fields[1])
        return list_names, list_passwords
                
    except Exception:
        return None, None
    pass

def display_users(names, passwords):
    # TODO 3/7
    if len(names) == 0: print('No user found')
    try:
        if len(names) != 0:
            print('No.  Name                Password\n',
                '----------------------------------')
        for i in range(len(names)):
            print(f'{i+1}    {names[i]: <20}{passwords[i]}')
    
    except Exception:
        print('No user found')
    pass

def valid_name(name):
    # TODO 4/7
    if len(name) < 3:
        return False
    for i in range(len(name)):
        if((ord(name[i]) >= 65 and ord(name[i]) <= 90) or (ord(name[i]) >= 97 and ord(name[i]) <= 122)):
            return True
        else:
            return False           
    pass

def generate_password(name):
    # TODO 5/7
    generated_password = name[0]
    generated_password += str(len(name))
    for _ in range(6):
        generated_password += chr(random.randint(33,122))
    return generated_password
    pass

def sign_up(file_name):
    # TODO 6/7
    count = 0
    try:
        with open(file_name, 'w') as file:
            while True:
                user_name = input('Enter name (\'s\' to Stop): ')
                if user_name == 's':
                    return count
                if valid_name(user_name) == False:
                    print('Name is invalid.')
                    continue
                    for line in file:
                        fields = line.rstrip('\n').split(',')
                        if user_name == fields[0]:
                            print('Name already exists.')
                user_password = generate_password(user_name)
                print(f'Hello {user_name}, your password is: {user_password}')
                file.write(f'{user_name},{user_password}\n')
                count += 1
            return count
    except Exception:
        return -1
    pass

def change_password(file_name, name, new_password):
    # TODO 7/7
    pass


USER_DB = 'C:/temp/assignment3_lastname.csv'

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
