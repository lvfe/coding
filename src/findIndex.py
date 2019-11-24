def findIndex(A,target):
    if len(A)==0 or target<=A[0]:
        return 0

    for i in range(0, len(A)-1):
        print(A[0])
        if target<=A[0]:
            print(A[0])
            return 0
        if target>A[i] and target<=A[i+1]:
            return i+1
    return len(A)

print(findIndex([2],5))