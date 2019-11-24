def ugly(n):
    current=1
    for i in range(1,n):
        j=current+1
        #for j in range(current+1,10000000):
        while isugly(j)!=True:
            j=j+1
        current = j
    return current
def isugly(j):
    if j==1:
        return True
    if j%2!=0 and j%3!=0 and j%5!=0:
        return False
    else:
        if j%2 ==0:
            isugly(j/2)
        elif j%3==0:
            isugly(j/3)
        else:
            isugly(j/5)

print(ugly(2))