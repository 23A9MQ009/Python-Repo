def is_automorphic(n):
    square = n ** 2
    if str(square).endswith(str(n)):
        return "Automorphic Number"
    else:
        return "Not an Automorphic Number"
n = int(input())
print(is_automorphic(n))
