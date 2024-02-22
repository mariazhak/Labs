# problem 1
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# problem 2
score = int(input("Enter a score: "))
if score < 60:
    print("The mark is F")
elif score >= 60 and score <= 69:
    print("The mark is D")
elif score > 69 and score <= 79:
    print("The mark is C")
elif score > 79 and score <= 89:
    print("The mark is B")
elif  score > 89 and score <=100:
    print("The mark is A")
else:
    print("Wrong score")

# problem 3
n = int(input("Enter n to find in Fibonacci sequence: "))
num1 = 1
num2 = 1
counter = 2
answer = 0

if n < 3 and n > 0:
    print("1")
elif n <= 0:
    print("Wrong input")
else:
    while counter < n:
        answer = num1 + num2
        num1 = num2
        num2 = answer
        counter += 1
    print("The", n, "Fibonacci number is", answer)

# problem 4
n = int(input("Enter number you want the factorial to know:"))
answer = 1
if n < 0:
    print("Wrong input")
elif n <= 1:
    print("The factorial is 1")
else:
    for i in range(1, n+1):
        answer = answer * i
    print("The factorial of", n, "is", answer)

# problem 5
n = int(input("How many rows in diamond do you want? (enter odd number)"))
if n%2 == 1:
    n = n+1
n = n//2

in_row_num = 2*n -1
for i in range(1,n+1):
    stars_num = 2*i - 1
    spaces_num = (in_row_num - stars_num)//2
    for j in range(0,spaces_num):
        print(" ", end="")
    for j in range(0,stars_num):
        print("*", end="")
    for j in range(0,spaces_num):
        print(" ", end="")
    print("")

for i in range(n-1, 0, -1):
    stars_num = 2*i - 1
    spaces_num = (in_row_num - stars_num)//2
    for j in range(0,spaces_num):
        print(" ", end="")
    for j in range(0,stars_num):
        print("*", end="")
    for j in range(0,spaces_num):
        print(" ", end="")
    print("")