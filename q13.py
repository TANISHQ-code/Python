def remove_value(lists,val):
    return[i for i in lists if i!=val]
list1 = [5, 20, 15, 20, 25, 50, 20]
res=remove_value(list1,20)
print(res)
