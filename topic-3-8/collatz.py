N = 999999
cone = 0
steps = 0
while (N != 1 and steps <= 1000 and cone <= 1000000):
    if (N % 2 == 0):
        N = N // 2 
    else:
        N = (N * 3) + 1
    if N > cone:
        cone = N
    steps = steps + 1

if steps > 1000 or cone > 1000000:
    N = "limit reached"

print(N)
print(cone)
print(steps)

