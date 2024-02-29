# task 5
my_info = {'first_name': 'Mariia', 'last_name': 'Zhak', 'age': 17, 'city': 'Kyiv'}
print("Student info:")
print("Name:", my_info['first_name'])
print("Surname:", my_info['last_name'])
print("Age:", my_info['age'])
print("City:", my_info['city'])

# task 6
programming_glossary = {'Loop': 'Structure which allows to run a block of code several times',
                        'Algorithm': 'A list of steps to solve the problem',
                        'Flowchart': 'A visual way to represent an algorithm',
                        'Recursion': 'Loop structure where a function calls itself',
                        'Tuple': 'An immutable data structure which stores an ordered sequence of values of different data types'}

print("Here are five programming terms:")
for key in programming_glossary:
    print(key, ":", programming_glossary[key])
