import threading, time
print("start")

def take_nap():
    time.sleep(5)
    print("get up")

thread_obj = threading.Thread(target = take_nap)
thread_obj.start()

print("end")
