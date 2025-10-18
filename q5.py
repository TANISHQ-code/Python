numbers = [12, 75, 150, 180, 145, 525, 50]
answer=[]
for x in numbers:
    if x%5==0 and x<=150:
        answer.append(x)
    elif x>150 and x<500:
        continue
    elif x>500:
        break
print(answer)
