'''
PROJECT EULER
    002

Task: Even Fibonacci Numbers
'''

def solve(max):
    sum = 0
    a = 1
    b = 2
    while b < max:
        if b % 2 == 0:
            sum += b
        tmp = b
        b += a
        a = tmp
    return sum

print(solve(4000000))
