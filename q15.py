str1 = "/*Jon is @developer & musician"
for char in str1:
    if char == char.isdigit() or char.isalpha() or ' ':
        print(char,end='')
