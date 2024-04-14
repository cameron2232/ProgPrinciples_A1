
def todos():
    print('==== TODO#1/4 ====')
    # TODO#1/4-Write a Task class so that when running the test code below, the
    #       following output will be produced:
    # Task: Save the world
    #         Difficulty: 7.3
    #         Done: False
    # Task: Learn Python
    #         Difficulty: 8.7
    #         Done: False
    task1 = Task(name='Save the world', difficulty='7.3')
    task2 = Task(name='Learn Python', difficulty='8.7')
    print(task1)
    print(task2)

    print('\n==== TODO#2/4 ====')
    # TODO#2/4-Write a SuperHero class so that when running the test code below, the 
    #       following output will be produced:
    # SuperHero: Spiderman
    #         Strength: 8.7
    #         Skills: ['time travel', 'fly', 'joking', 'eat pizza']
    hero1 = SuperHero(name='Spiderman', strength='8.7', 
        skills=['time travel', 'fly', 'joking', 'eat pizza'])
    print(hero1)

    print('\n==== TODO#3/4 ====')
    # TODO#3/4-Add code to SuperHero class so that when running the test code
    #       below, the following output will be produced:
    # SuperHero: Spiderman
    #         Strength: 8.7
    #         Skills: ['time travel', 'fly', 'joking', 'eat pizza']
    #         Tasks: ['Save the world', 'Learn Python']
    hero1.assign_task(task1)
    hero1.assign_task(task2)
    print(hero1)

    print('\n==== TODO#4/4 ====')
    # TODO#4/4-Add more code to the two classes so that when running the test
    #       code below, the following output will be produced:
    # SuperHero: Spiderman
    #         Strength: 8.7
    #         Skills: ['time travel', 'fly', 'joking', 'eat pizza']
    #         Tasks: ['Save the world', 'Learn Python']
    # Task:   Save the world
    #         Difficulty: 7.3
    #         Done: True
    hero1.complete_task(task1)
    print(hero1)
    print(task1)

todos()