import time

from math import factorial as f

start = time.time()

counter = 0


def ncr(n, r):
    return f(n)/(f(r)*f(n-r))

for n in range(23, 101):
    for r in range(4, n-3):
        if ncr(n, r) > 1000000:
            counter += 1

print (counter)

end = time.time()

print (end - start)