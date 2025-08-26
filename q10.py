list1=[10,20,25,30,35]
list2=[40,45,60,75,90]
result=[]
for i in range(0,5):
    if not list1[i]%2==0:
        result.append(list1[i])
    else:
        continue
for j in range(0,5):
    if list2[j]%2==0:
        result.append(list2[j])
    else:
        continue

print(result)
