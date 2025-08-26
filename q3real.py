str=input("pls enter your string ")
print(f"your given string is {str}")
print("printing only even indexed characters")
for x in range(len(str)):
    if x%2==0:
        print(str[x])
    else:
        continue
    