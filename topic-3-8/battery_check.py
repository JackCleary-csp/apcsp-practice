charges = [62, 28, 85, 14, 47]
low = charges[0]
high = charges[0]
below_30 = 0
atleast80 = 0
avg = 0
total = 0

for charge in charges:
    if charge > high:
        high = charge
    if charge < low:
        low = charge
    if charge < 30:
        below_30 = below_30 + 1
    if charge >= 80:
        atleast80 = atleast80 +1

avg = (sum(charges) / len(charges))
total = sum(charges)

print(high)
print(low)
print(below_30)
print(atleast80)
print(avg)
print(total)