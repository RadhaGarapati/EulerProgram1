def solution(X, A):
    listarray = list(range(1, X + 1))
    if X < 1 or len(A) < 1:
        return -1
    found = -1
    for element in listarray:
        if element in A:
            if A.index(element) > found:
                found = A.index(element)
        else:
            return -1
    return found


X = 5
A = [1, 2, 4, 5, 3]
solution(X, A)
print(solution(X, A))
