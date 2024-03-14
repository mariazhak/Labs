# reading file contents as one string
with open('learning_python.txt') as f:
    print(f.read())
    print('')

# reading file contents by iterating over the file
with open('learning_python.txt') as f:
    for line in f:
        print(line, end='')
    print('')

# reading file contents in the list
with open("learning_python.txt") as f:
    data_list = f.readlines()

print('')
# iterating over the list outside the with block
for element in data_list:
    print(element, end='')
