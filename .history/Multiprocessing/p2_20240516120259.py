import time
import multiprocessing

def sleep_for_a_bit(seconds):
    print(f"Sleeping {seconds} second(s)")
    time.sleep(seconds)
    print("Done Sleeping")

p1 = multiprocessing.Process(target=sleep_for_a_bit,args=[1])    

processes = []


finish = time.perf_counter()
print("Finished running after seconds :", finish)    