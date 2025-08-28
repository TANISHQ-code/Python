def sum(a):
    if a:
        return a+sum(a-1)
    else:
        return 0
print(sum(10))
