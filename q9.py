def get_min_max(numbers):
    mini=min(numbers)
    maxi=max(numbers)
    tuple1=(mini,maxi)
    return tuple1

# Test the function
my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")
