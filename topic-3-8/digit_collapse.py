n = 9875
finnburger_sum = 0

while n >= 10:
    finnburger_passes = 0
    while n > 0:
        finnburger_passes = finnburger_passes + n % 10
        n = n // 10
    finnburger_sum += 1
    n = finnburger_passes

print(finnburger_sum)
print(finnburger_passes)    
