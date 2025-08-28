def factorial(x):
    if x<0:
        return
    elif x:
        return x*factorial(x-1)
    else:
        return 1
num=int(input("write a number to find its factorial?"))
ans=factorial(num)
print(ans)