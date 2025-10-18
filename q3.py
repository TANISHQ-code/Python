characters=[]
while True:
    item=input("pls write the list of charecters press 'Q'to exit")
    if item.lower()=='q':
        break
    else:
        characters.append(item)
print(f"orignal string is {characters}")
print("printing only even indexed characters")

for x in characters:
    if characters.index(x)%2==0:
        print(x)
    else:
        continue