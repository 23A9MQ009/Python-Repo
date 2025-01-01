def is_ugly_number(n):
    if n <= 0:
        return False
    for i in [2, 3, 5]:
        while n % i == 0:
            n //= i
    return n == 1
num = int(input())
if is_ugly_number(num):
    print("Ugly Number")
else:
    print("Not Ugly Number")
