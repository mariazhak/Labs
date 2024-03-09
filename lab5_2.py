def fibonacci_recursion(n):
    """Finds the nth Fibonacci number using recursion"""
    if n<=2:
        return 1
    else:
        return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)

def fibonacci_iterative(n):
    """Finds the nth Fibonacci number using list storing"""
    fib_list= [1, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list[-1]

n = int(input("Enter n (which Fibonacci number you want to know, first Fibonacci number is 1): "))
print(f"{n} fibonacci number found by recursion is:", fibonacci_recursion(n))
print(f"{n} fibonacci number found by storing data in list is:", fibonacci_iterative(n))