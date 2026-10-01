a = 48
b = 18
repeats = 0

while b != 0:
    a <= 1000000 and b <= 1000000
    temp = a % b
    a = b
    b = temp
    repeats = (repeats + 1)

print(a)
print(repeats)