def check(s1,s2):
    count=0
    for char in s1:
        if char in s2:
            count+=1
    print(count==len(s1))
s1 = "Yn"
s2 = "PYnative"
check(s1,s2)

