import time
timer=int(input("set your timer in seconds"))
for x in range(timer,0,-1):
    hours=int((x/(60*60))%60)
    minutes=int((x/60)%60)
    seconds=int(x%60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIMES UPP!!")