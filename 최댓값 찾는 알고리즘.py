def find_max(A):
    max = A[0]
    for i in range(len(A)):
        if A[i] > max :
            max = A[i]

    return max

find_max([5, 7, 8, 4, 2])
