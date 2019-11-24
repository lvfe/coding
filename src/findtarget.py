def search(A, target):
    # write your code here
    start =0
    if A==[]:
        return -1
    rotata = 0
    fla=False
    while A[rotata]<A[rotata+1]:
        fla=True
        rotata = rotata+1
    if fla == True:
        rotata = rotata+1
    if rotata!=len(A)-1:
        arr = A[rotata:]+A[:rotata]
    else:
        arr= A
    print(arr)
    end=len(arr)-1
    middle=(start+end)//2
    if arr[0]==target:
        return len(arr)-rotata-1
    if arr[end]==target:
        return end-rotata-1
    if arr[end]<target and arr[0]>target:
        return -1
    while start < end:
        middle=(start+end)//2
        if arr[middle]==target:
            print(middle)
            return (middle-rotata+len(arr))%len(arr)-1
        elif arr[middle]<target:
            start = middle
        else:
            end = middle

    return -1
print(search([4, 5, 1, 2, 3],2))