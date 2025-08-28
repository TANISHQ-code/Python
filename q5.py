def outer_function(a, b):
    # Inner function to calculate sum
    def inner_function(x, y):
        return x + y

    # Call inner function
    result = inner_function(a, b)

    # Add 5 to the result
    result += 5

    return result


# Example usage
print(outer_function(3, 7))   # (3 + 7) + 5 = 15
print(outer_function(10, 20)) # (10 + 20) + 5 = 35
