def sortindex(A):
    if len(A)<=1:
        return A
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            if A[i]>A[j]:
                t = A[j]
                A[j]=A[i]
                A[i]=t
    return A
print(sortindex([3,1,2]))