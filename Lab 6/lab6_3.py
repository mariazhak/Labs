f = open('learning_python.txt')
data = f.readlines()
print('The amount of lines is', len(data))

# counting the amount of words
words = []
for line in data:
    words.extend(line.split(' '))
print('The amount of words is', len(words))


# counting the amount of characters
characters = 0
for line in data:
    characters += len(line)
print('The amount of characters is', characters)
