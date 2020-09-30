import math, time


def pathcounter(gridsize):
    p = math.factorial(gridsize * 2) / (math.factorial(gridsize) ** 2)
    return p


tic = time.clock()
n = pathcounter(20)
toc = time.clock()
elapsed = toc - tic
print("%s found in %s seconds" % (n, elapsed))
