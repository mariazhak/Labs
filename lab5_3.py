def factorial_recursive(num):
    """Finds factorial of a number using recursion"""
    if num == 1:
        return 1
    return num * factorial_recursive(num-1)

def factorial_iterative(num):
    """Finds factorial of a number using list"""
    fact_list = [1]
    for i in range(1, num+1):
        fact_list.append(fact_list[i-1]*i)
    return fact_list[-1]

n =  int(input("Enter the number which you want to find the factorial: "))
print(f"The factorial of {n} using recursion is", factorial_recursive(n))
print(f"The factorial of {n} using list saving is", factorial_iterative(n))