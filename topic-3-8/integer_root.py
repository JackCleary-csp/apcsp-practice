n = 16

lower = 1
upper = 1001

while upper - lower > 1:
    midpoint = (lower + upper) // 2
    if midpoint * midpoint <= n:
        lower = midpoint
    else:
        upper = midpoint

print(lower)