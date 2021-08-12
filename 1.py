def S(r, x):
    return ((x + (r//x)*x)/2) * (r//x)
def sum_multiple(r, x, y):
    r = r - 1
    z = x * y
    return int(S(r, x) + S(r, y) - S(r, z))

print(sum_multiple(1000, 3, 5))