list=[]
n=int(input("pls enter the number of terms"))
for x in range(0,n):
    x=int(input("enter the term"))
    list.append(x)
print("the list of numbers divisible by 5 are :")
for i in range (0,n):
    if list[i]%5==0:
        print(list[i])
    else:
        continue
