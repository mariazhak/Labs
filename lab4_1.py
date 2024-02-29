# in this implementation it is not necessary for user to input the number n itself.
# I could implement the input of n, and in average divide by n, not by len(str_input)
str_input = input("Enter numbers separated by space: ")
str_input = str_input.split(" ")
sum = 0
for i in str_input:
    sum += int(i)

print("The sum is ", sum)
print("The average is ", sum/len(str_input))