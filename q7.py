str_x=input("pls enter your statement")
a=0
for i in range (len(str_x)):
    if str_x[i]=='e':
        if str_x[i+1]=='m':
            if str_x[i+2]=='m':
                if str_x[i+3]=='a':
                    a+=1
        else:
            continue
print(a)
#use count keyword next time