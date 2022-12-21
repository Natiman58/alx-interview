"""
    A function that returns a list of integers representing the pascal's triangle
"""

def pascal_triangle(n):
    """ generate the pascal's triangle"""
    x = []
    if n <= 0:
        return x
    else:
        for i in range(n+1):
            for j in range(n-i):
                print(' ', end='')

        C = 1
        for j in range(1, i+1):
             print(C, ' ', sep='', end='')
             C = C * (i - j) // j
        print()
