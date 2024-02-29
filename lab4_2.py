str_input = input("Enter your list separated by space: ")
str_list = str_input.split(" ")
m = int(input("Enter number you want to multiply by: "))

print("Your list is:", end = " ")
for i in str_list:
    print(int(i), end= " ")
print("\nYour list in Python format is: ", str_list)

print("Your list after multiplying:", end = " ")
for i in range (len(str_list)):
    str_list[i] = int(str_list[i]) * m
    print(str_list[i], end = " ")
print("\nYour list after multiplying in Python format:", str_list)
