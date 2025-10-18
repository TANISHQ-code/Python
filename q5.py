list=[]
n=0
while True:
    integer=int(input("enter integer values press 69 to exit (press "" to continue)"))
    if integer==69:
        break
    else:
        list.append(integer)
        n+=1
if list[0]==list[n-1]:
    print("TRUE")
else:
    print("FALSE")
