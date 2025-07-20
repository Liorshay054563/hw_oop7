
import threading
import time

def print_sequence(name,count):
    for i in range(count):
        print(f"Thread <{name}> i : =<{i}> ")
        time.sleep(0.3)

t1= threading.Thread(target=print_sequence,args= ("Alpha",5, ))
t2= threading.Thread(target=print_sequence,args= ("Beta",3, ))
t3= threading.Thread(target=print_sequence,args= ("Gamma",4, ))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


print("end 1")

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=2) as executor:

    executor.submit(print_sequence, "Alpha", 5)
    executor.submit(print_sequence, "Beta", 3)
    executor.submit(print_sequence, "Gamma", 4)




