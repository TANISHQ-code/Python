str1 = "PYnative29@#8496"
count=0
no_of_digits=0
for char in str1:
    if char.isdigit():
        count+=int(char)
        no_of_digits+=1
avg=count/no_of_digits
        
print(f"sum of digits={count}")
print(f"average={avg}")

