print('Hi! Enter the names of all users please!')
checker = input('Enter 1 user name(or enter e/E to exit): ')
counter = 1
output = open('output.txt', 'w')
while checker != 'e' and checker != 'E':
    output.write(f'User {counter}:' + checker + '\n')
    counter += 1
    checker = input(f'Enter {counter} user name(or enter e/E to exit): ')

