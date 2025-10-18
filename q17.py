tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
list1=list(tuple1)
sorted_list=sorted(list1,key=lambda item: item[1])
print(sorted_list)



