def add_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    print(num)

num = int(input())
add_digits(num)
