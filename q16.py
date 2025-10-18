list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
new_list=[]
for rows in list_of_lists:
    for elements in rows:
        new_list.append(elements)
print(new_list)
