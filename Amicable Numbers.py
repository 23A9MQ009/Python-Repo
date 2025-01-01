def sum_of_divisors(n):
    divisors_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != 1 and i != n // i:
                divisors_sum += n // i
    return divisors_sum
def check_amicable(n, m):
    if sum_of_divisors(n) == m and sum_of_divisors(m) == n:
        return "Amicable"
    else:
        return "Not Amicable"
n = int(input())
m = int(input())
print(check_amicable(n, m))
