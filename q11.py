def get_min_max(numbers):
    tuple1=tuple(numbers)
    return min(numbers),max(numbers)

list1 = [10, 5, 20, 2, 15]
min_max_values = get_min_max(list1)
print(f"Original numbers: {list1}")
print(f"Minimum and maximum values: {min_max_values}")