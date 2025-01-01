import math
def is_pronic(x):
    n = int(math.sqrt(x))
    if n * (n + 1) == x:
        return "YES"
    else:
        return "NO"
x = int(input())
print(is_pronic(x))
