def digcount(k,n):
    count=0
    for i in range(0,n+1):
        tmp = i
        while tmp>0:
            if tmp%10==k:
                count=count+1
            tmp=tmp//10
    return count
print(1,9)