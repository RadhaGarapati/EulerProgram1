import time

start = time.time()

i = 1


while True:
    if set(str(i)) == set(str(6 * i)):
        if set(str(i)) == set(str(5 * i)):
            if set(str(i)) == set(str(4 * i)):
                if set(str(i)) == set(str(3 * i)):
                    if set(str(i)) == set(str(2 * i)):
                        print(i)
                        break
    i += 1

end = time.time()

print(end - start)
