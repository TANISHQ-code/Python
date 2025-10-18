my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,120]
new_list=[]
for x in range(0,len(my_list)):
    if x%2!=0:
        new_list.append(my_list[x])
    else:
        continue
print(new_list)