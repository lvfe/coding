import math
def narcissitic(n):
    resultlist = []
    #print(pow(10,n-1))
    if n==1:
        resultlist.append(0)
    for i in range(pow(10,n-1),pow(10,n)):
        temp=i
        list=[]
        while temp>0:
            list.append(temp%10)
            temp=temp//10
        sum=0
        #print(list)
        for j in range(n):
            if list[j]!=0:

                anum=math.pow(list[j],n)
                sum+=anum
        if sum == i:
            resultlist.append(i)
    return resultlist
print(narcissitic(2))