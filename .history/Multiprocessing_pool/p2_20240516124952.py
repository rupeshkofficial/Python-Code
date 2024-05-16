from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x

    return sum

if __name__ == "__main__":
    t1 = time.time():
    p = Pool()
    array = [1,2,3,4,5]
    p = Pool()
    result = p.map(f, array)
    print(result)
