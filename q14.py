str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_list=[]
for obj in str_list:
    if obj:
        new_list.append(obj)
print(new_list)
