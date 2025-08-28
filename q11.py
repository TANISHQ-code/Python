def print_info(**kwargs):
    if kwargs:
        print("infooo..")
        for key,value in kwargs.items():
            print(f"{key}:{value}")
    else:
        print("no info provided")

print_info(name="Alice", age=30, city="New York")
print_info(job="Engineer", salary=75000)
print_info(country="USA", state="California", zip_code="90210")
print_info()  # Call with no arguments
 