def is_unique(n):
    if len(set(str(n))) == len(str(n)):
        return "Unique Number"
    else:
        return "Not Unique Number"
n = int(input())
print(is_unique(n))
