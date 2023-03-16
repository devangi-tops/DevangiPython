def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))

n = int(input('Enter a number here: '))
if n <= 0:
    print('Factorial of numer less than 1 does not exists')
else:
    print("Factorial of given numer is",fact(n))
