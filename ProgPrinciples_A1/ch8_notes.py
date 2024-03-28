# String

# 1. Basics
# - what: a sequence of characters
#   - Character: map 'a' --> integer, unicode, utf-8, ASCII
#   - functions: ord(char) --> int, chr(int) --> char
# - accessing: indexing string[ind], slicing [:], len()
#   - loop over: for in, for in range
#   - string is immutable
# - * and +
# - random: choice(), choices(k), sample(k)

import random

def string_basics():
    # ord() and int()
    i1 = ord('a')
    c1 = chr(48)
    print(i1, c1)
    #for i in range(2 ** 16):
        #print(chr(i), end = ' ')
        
    # indexing, slicing, len, for
    s1 = 'Hello Pythoner'
    c2 = s1[0]
    subs1 = s1[6:]
    #for i in range(len(s1)):
    #    print(s1[i], end = ' ')
    for char in s1:
        print(char, end = ' ')
    #s1[0] = 'h' # TypeError
    print (c2, subs1)
    
    # + and *
    s1, s2 = 'abc', '123'
    s3 = s1 + s2 # concactenation
    s4 = s3 * 4
    print (s3, s4)
    
    import random
    s1 = 'jsnfw34thq9834heinw43dfha7a4r]-=]d[fasdfasdf'
    c1 = random.choice(s1)
    l1 = random.choices(s1, k = 10) # list of characters
    l2 = random.sample(s1, k = 10)
    print(c1, l1, l2)
    s2 = '-'.join(l1)
    s3 = ''.join(l2)
    print(s2, s3)
    
def exercise_p13():
    num = int(input('Enter an int: '))
    counters = [0] * 10
    for c in str(num):
        # '0' -> counters[0] + 1, '1' -> countres[1] + 1, ...
        counters[int(c)] += 1
    print(counters)
    
def exercise_p13_p2():
    firstname = 'Jack'
    lastname = 'Anna'
    student_id = 909835974
    login_name = firstname[:3] + lastname[:3] + str(student_id)[-3:]
    print(login_name)
    
def exercise_1():
    charset = 'qwertyuiop0987654321asdfghjklzxcvbnm'
    with open('random.txt', 'w') as f:
        for _ in range(10000):
            f.write(''.join(random.choices(charset, k=random.randint(3, 10))) + ' ')
    counters = [0] * len(charset)
    with open('random.txt', 'r') as f:
        s1 = f.read()
    for c in s1:
        for i in range(len(charset)):
            if c == charset[i]:
                counters[i] += 1
    print(charset)
    print(counters)
    
# 2. string operations
# - n / not in
# - string methods:
#   - return T/F: islower(), isupper(), isdigit()
#                   isalpha(), isalnum(), isspace()
#   - return new string: rstrip(), lstrip(), strip()
#       upper(), lower()
#   - searching: index(), find(),
def string_operations():
    # in, not in
    heroes = 'spiderman, ironman, superman, hulk, thor'
    if 'man' in heroes: print('there are men in heroes')
    s1 = 'ABC234abc@#$%'
    s2, s3, s4 = 'abcxyz', '87683294563', 'WETUJNDSF'
    print(s1.isupper(), s1.islower(), s1.isdigit(), s1.isalpha(), s1.isalnum(), s1.isspace())
    print(s2.isupper(), s2.islower(), s2.isdigit(), s2.isalpha(), s2.isalnum(), s2.isspace())
    
    s1 = '====hello world===='
    print(s1.rstrip('='), s1.lstrip('='), s1.strip('='))
    print(s1.upper(), s1.lower())
    
    heroes = 'spiderman, ironman, superman, hulk, thor'
    
    birthday = '2004/12/23'
    date = birthday.split('/')
    print(date)
    
    number = '1-905-123-4567'
    codes = number.split('-')

def main():
    #string_basics()
    #exercise_p13()
    #exercise_p13_p2()
    exercise_1()
    string_operations()
main()