import math
def is_perfect_square(n):
    if n < 0:
        return False
    root = math.isqrt(n) 
    return root * root == n
num = int(input())
if is_perfect_square(num):
    print("True")
else:
    print("False")
