for x in range(0,11):
    if x==0:
        print(f"current number={x},previous number={x},sum={x}")
    else:
         print(f"current number={x},previous number={x-1},sum={x+(x-1)}")