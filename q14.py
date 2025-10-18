students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
above=[]
for x in range(3):
    if students[x][1]>=90:
        above.append(students[x])
print(above)
