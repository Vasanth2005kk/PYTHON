import time 

for i in range(10,-1,-1):
    time.sleep(1)
    print(str(i).center(100))
else:
    print("HAPPY CODING!".center(100))