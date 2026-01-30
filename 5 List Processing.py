# Task 5: Store 5 numbers in a list and sort from highest to lowest.
numbers = []

for i in range(5):
    val = float(input(f"Input number {i+1}: "))
    numbers.append(val)

# Sorting the list in descending order
numbers.sort(reverse=True)

print("Numbers from highest to lowest:", numbers)