start=int(input("start of the range ?? "))
end=int(input("end of the range ?? "))
a=0
for x in range (start,end+1):
    a=0
    if x>1:
        for y in range(2,x):
         if x%y==0:
            break
         else:
            a+=1

        if a==x-2:
            print(x,end=" ")
            
    else:
        continue
