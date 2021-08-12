def divisor(n):
    x = sum([i for i in range(1,n) if not n % i])
    return x

arr = []
for i in range(28123):
    arr.append(False)
for i in range(12):
    arr[i] = True
for i in range(28123):
    d = divisor(i+1)
    print(i+1, d) 
    if d > i+1:
        arr[i] = True
        print("true")
    else:
        arr[i] = False
a = []
for i in range(28123):
    a.append(False)

for i in range(28123):
    for j in range(28123):
        if arr[i] and arr[j] and (i + j < 28123):
            a[i + j] = True
#print(divisor(10))
s = 0
for i in range(2812):
    if a:
        s += a[i]

print(s)