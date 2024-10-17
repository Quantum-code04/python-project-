import time
hrs=int(input("Enter a Hours :"))
minu=int(input("Enter a Minutes :"))
sec=int(input("Enter a Seconds :"))
x=(hrs*60*60)+(minu*60)+(sec)
for i in range (x,0,-1):
    sec=i%60
    minu=int(i/60)
    if minu>=60:
        minu=(int(minu%60))
    else:
        minu=(minu)
    hrs=int(i//3600)
    print(f"{hrs:02}:{minu:02}:{sec:02}")
    time.sleep(1)
   
print("timee's up")
    
    
