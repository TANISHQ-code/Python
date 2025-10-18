string1 = 'Jessa'
freq_dict={}
for char in string1:
    if string1.count(char)>1:
        freq_dict[char]=string1.count(char)
    else:
        freq_dict[char]=1
print(freq_dict)
