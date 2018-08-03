import balloon
import time 

balloon = balloon.Ballon()
i = 0;
while True:
    balloon.send(True)
    print("before")
    time.sleep(2)
    print("after")
    balloon.send(False)
    time.sleep(2)
    i = i +1
    if i == 3:
        del balloon
        break;
