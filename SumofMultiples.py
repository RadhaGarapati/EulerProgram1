end = 1000

def Solution01():
    
    sum = 1
    for i in range(1,end):
        if isMultiple(i):
            sum += i 
    #print(solution01())
    print(sum)
print(Solution01())
def isMultiple(i):
   return (i % 3 == 0) or (i % 5 == 0)