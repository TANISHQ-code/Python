def largest(list=[]):
    result=list[0]
    for x in list:
        if x>result:
            result=x
    return result
x = [4, 6, 8, 24, 12, 2]
ans=largest(x)
print(ans)