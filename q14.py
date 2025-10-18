my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
new_list=[i for i in my_list if isinstance(i,(int,float))]
print(new_list)
