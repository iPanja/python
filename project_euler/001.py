'''
PROJECT EULER
    001

Task: Multiples of 3 and 5
'''

def solve(max):
    sum = 0
    for x in range(0, max):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum

print(solve(1000))
