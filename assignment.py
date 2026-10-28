def replace_value(values, index, new_value):
    values[index] = new_value

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def summarize(values):
    return min(values), max(values), sum(values)


days = int(input("Enter the number of days: "))

original = []
for i in range(days):
    val = int(input("Enter water use in litres: "))
    original.append(val)

updated = original[:]

idx = int(input("Enter the index to correct: "))
new_val = int(input("Enter the new water use: "))
replace_value(updated, idx, new_val)

target = int(input("Enter the water use to search for: "))

first_idx = find_first(updated, target)
counts = updated.count(target)

sorted_lst = sorted(updated)
minimum, maximum, total = summarize(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_lst}")
print(f"Minimum water use: {minimum} litres")
print(f"Maximum water use: {maximum} litres")
print(f"Total water use: {total} litres")

if first_idx == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_idx}")

print(f"Matching values: {counts}")