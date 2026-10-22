def count_below(values, threshold):
    count = 0
    for value in values:
        if value < threshold:
            count = count + 1
    return count
def count_at_least(values, threshold):
    count = 0

charges = [62, 28, 85, 14, 47]
low_count = count_below(charges, 30)
print(low_count)
print(count_below(charges, 30))