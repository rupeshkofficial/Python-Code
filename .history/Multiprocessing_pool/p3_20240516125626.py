from multiprocessing import Pool

def f(n):
    return n*n

if __name__ == "__main__":
     p = Pool(processes=)
    array = [1,2,3,4,5]
   
    result = p.map(f, array)
    print(result)
