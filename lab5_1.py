def sumN(n):
    """Finds the sum of the first n natural numbers using iteration"""
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

def sumNFormula(n):
    """Finds the sum of first n natural numbers using formula"""
    return n*(n+1)//2

def sumNCubes(n):
    sum_cube = 0
    for i in range(1,n+1):
        sum_cube = sum_cube + i**3
    return sum_cube

n = int(input("Enter n:"))
print(f"The sum of the first {n} natural numbers is", sumN(n))
print(f"Using formula, the sum of the first {n} natural numbers is", sumNFormula(n))
print(f"The sum of the cubes of the first {n} natural numbers is", sumNCubes(n))