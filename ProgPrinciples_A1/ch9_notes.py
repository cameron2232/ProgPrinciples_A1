# Annoucements:
#   - no lecture next class on Wed, just a Q&A session
#   - Final exam next week on Mon

# Ch9 - Dictionaries
#   - a collection of key:value pairs 
#   - retrieve values using keys (use index to access elements in list)
#   - create: {key1:value1, key2:value2, ... }
#       - key: immutable (int, float, str, tuple)
#       - key (values) can be of different types
#       - nested dict (value can be a dict)
#       - merge two dicts into a new one: |
#       - NOTE: key must be unique 
#   - retrieve/insert/update: use the key, dict[key]
#       - get: dict.get(key, default_value)
#   - delete: del, pop(key, default), popitem(), clear()
#   - NOTE: items in dict are ordered (since version 3.7)
#   - operations: len(dict), key in/not in dict 
#   - loop-over: using for loop
#       - for key in dict, for key in list(dict), for key in dict.keys()
#       - for v in dict.values(), for k, v in dict.items()
#   - comprehension: easier way to get new dict from existing one

def about_dict():
    # create a dict
    # course code:course name
    courses = {'prog10004': 'Programming foundations',
               'dbas14444': 'Database management',
               'eng12345': 'Computer English'}
    # student id: student name
    students = {987123: 'Spiderman', 987124: 'Superman',
                987125: 'Hulk'}
    # mixed types in dict 
    stud_info = {987123: 'Hongha hongha',
                 'gpa': 3.87}
    # nested dict
    contacts = {'spiderman': {
                        'email': 'spider@man.com',
                        'phone': 9051234567,
                        'intgram': 'spiderman12345'
                    },
                'hulk' : {
                        'address': '123 main str.',
                        'discord': 'hulk1324345'
                }}
    # merge: |
    dict1 = {1:'a', 2:'b', 3:'c'} # key 3
    dict2 = {'a':123, 'b': 234, 'c': 345, 3:'abc'} # key 3
    dict3 = dict1 | dict2 
    print(dict3) # 3:'abc'

    # accessing values using keys
    # course:mark
    marks = {'python': 92.3, 'database': 87.6, 'math': 74.5}
    db_mark = marks['database'] # lst[1]
    # eng_mark = marks['english'] # key not in dict, KeyError: 'english'
    eng_mark = marks.get('english', 'English is not in dict')
    print(eng_mark) # English is not in dict
    marks['english'] = 56.78 # insert 
    marks['python'] = 97.89  # update
    print(marks) # {'python': 97.89, 'database': 87.6, 'math': 74.5, 'english': 56.78}
    del marks['python']
    print(marks.pop('database')) # 87.6
    print(marks.popitem()) # ('english', 56.78)
    print(marks) # {'math': 74.5}

    # len(), in/not in, for-loop
    # abbre:full name
    days = {'Mon': 'Monday', 'Tue': 'Tuesday',
             'Wed': 'Wednesday', 'Thu': 'Thursday',
             'Fri': 'Friday', 'Sat': 'Saturday',
             'Sun': 'Sunday'}
    print(len(days), 'Jan' in days, 'Sun' not in days) # 7, False, False

    # for key in dict:
    for d in days:
        print(d, '=', days[d])
    for k in list(days): # convert dict to list of keys
        print(k, ':', days[d])
    for key in days.keys(): # .keys()
        print(key, '-', days[key])
    for value in days.values(): # .values()
        print(value)
    for item in days.items(): # items, 0-key, 1-value
        print(item[0], '>', item[1]) 
    for k, v in days.items(): # probably most commonly used
        print(k, '#', v)

    # Comprehension
    names = ['Anna', 'Banna', 'Canna', 'Danna']
    marks = [3.3, 4.4, 5.5, 6.6]
    # name:mark
    d1 = {}
    for i in range(len(names)):
        d1[names[i]] = marks[i]
    print(d1) # {'Anna': 3.3, 'Banna': 4.4, 'Canna': 5.5, 'Danna': 6.6}

    d2 = {names[i]:marks[i] for i in range(len(names))} # dict comprehension
    print(d2)

    d3 = {k: v * 2 for k, v in d2.items()}
    print(d3) # {'Anna': 6.6, 'Banna': 8.8, 'Canna': 11.0, 'Danna': 13.2}


def main():
    about_dict()
main()
