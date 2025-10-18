def new_string(s1,s2):

    s3=s1[0]+s2[-1]+s1[1]+s2[-2]+s1[2:]+s2[0:len(s2)-2]
    print(s3)
s1 = "Abc"
s2 = "Xyz"
new_string(s1,s2)
