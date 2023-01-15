def square(n):
    '''
    calculates the square of the number up to n
    '''
    return [i ** 2 for i in range(n)]

print(square(10))