my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
del my_dict['profession']
print(my_dict)
for key,value in my_dict.items():
    print(f"{key}:{value}",end=' ')
print()
check='age' in my_dict
print(f"does age exist??:{check}")
