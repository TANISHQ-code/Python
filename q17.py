num=int(input("write in number"))
n=int(input("print the number of terms"))

ans=0
real_ans=0
y=num
for x in range (1,n+1):
    
    ans+=y
    real_ans+=ans
    y*=10
print(real_ans)
