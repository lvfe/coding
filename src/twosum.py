def twosum(A,target):
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]+A[j]==target:
                return [i,j]

print(twosum([2,7,11,15],9))