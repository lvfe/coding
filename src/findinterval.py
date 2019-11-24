def findinterval(A):
    sorted(A, key=lambda key:key[0])
    A.sort()
    print(A)
    lista = []
    if len(A)<=1:
        return len(A)
    start = 0
    sum=[]
    find(A,start,sum)
    return sum
def find(A,start,sum):
    if start==len(A)-1:
        return
    for i in range(start+1,len(A)):
        if A[start][1]<A[i][0]:
            if [A[start],A[i]] in sum:
                break
            sum.append([A[start],A[i]])
        find(A,i+1,sum)
print(findinterval([(1,5), (4,8), (5,12)]))
print(findinterval([(27,74),(25,65),(8,36),(21,63),(18,20),(35,51),(55,86),(49,69),(79,89)]))