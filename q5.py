str1 = "P@#yn26at^&i5ve"
alphabets=0
digits=0
symbol=0
for char in str1:
    if char.isalpha():
        alphabets+=1
    elif char.isdigit():
        digits+=1
    else:
        symbol+=1
print("no of alphabets,digits and symbols are : ")
print(f"alphabets={alphabets}")
print(f"digits={digits}")
print(f"symbol={symbol}")

