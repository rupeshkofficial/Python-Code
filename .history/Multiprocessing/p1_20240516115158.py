import time
import multiprocessing

def sleep_for_a_bit(seconds):
    print(f"Sleeping {seconds} second(s)")
    time.sleep(seconds)
    print("Done Sleeping")

p1 = multiprocessing.Process(target=sleep_for_a_bit,args=[1])    
p2 = multiprocessing.Process(target=sleep_for_a_bit,args=[1])    

if __name__ == ''