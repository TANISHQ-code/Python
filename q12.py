income=float(input("pls enter your input"))
if income<=10000:
    print("chal be gareeb")
else:
    tax=10000*0+(10000*10)/100+((income-20000)*20)/100
    print(f"you owe {tax}")