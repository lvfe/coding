def findsingle(A):
    A.sort()
    print(A)
    i = 0
    while i<len(A)-1:
    #for i in range(0,len(A)):
        #print(i)
        if A[i]==A[i+1]:
            i=i+2
        else:
            break
    return A[i]

print(findsingle([1,1,2,2,3,4,4]))