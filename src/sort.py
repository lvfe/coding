def sortarray(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i][1]<arr[j][1]:
                t=arr[j]
                arr[j]=arr[i]
                arr[i]=t
            if arr[i][1]==arr[j][1]:
                if arr[i][0]>arr[j][0]:
                    t=arr[j]
                    arr[j]=arr[i]
                    arr[i]=t
    return arr
print(sortarray([[2,50],[1,50],[3,50]]))
