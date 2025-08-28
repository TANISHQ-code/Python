def even_check(a,b):
    even=[]
    for x in range(a,b+1):
        if x%2==0:
            even.append(x)
    return even
result=even_check(4,30)
print(result)