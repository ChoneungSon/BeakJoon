import time
start = time.time()
A = ['a', 'b', 'd', 'c']


B = [0]*100000
for i in range(100000):
    # for j in range(i, 100000):
    B[i] += 1
print((time.time()-start)*100000//60)