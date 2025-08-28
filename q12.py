global_var = 10

def modify_global_var():
    global global_var
    global_var = 20
    print("Inside function:", global_var)

modify_global_var()
print("Outside function:", global_var)