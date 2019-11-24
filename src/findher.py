def findher(A):
    # finds
    sP=[]
    tP=[]
    depth=0
    for i in range(len(A)):
        if "S" in A[i]:
            sP=[i,A[i].index("S")]
            break
    for i in range(len(A)):
        if "T" in A[i]:
            tP=[i,A[i].index("T")]
            break
    #print(A)
    result = False
    find(A,sP,depth,tP, result)

    if "T" not in "".join(A):
        return True
    return False
def find(A,sP,depth,tP, result):
    print(A)
    if depth>len(A)+len(A[0]):
        return False
    if sP[0]==tP[0]and sP[1]==tP[1]:
        return True
    # up, down, left, right
    if tP[1]<sP[1] and sP[1]!=0 and A[sP[0]][sP[1]-1]!="*":
        orgin=list(A[sP[0]])
        orgin[sP[1]]="."
        orgin[sP[1]-1]="S"
        A[sP[0]] = "".join(orgin)

        sP[1]=sP[1]-1

        find(A,sP,depth+1,tP,result)

        orgin=list(A[sP[0]])
        orgin[sP[1]]="."
        orgin[sP[1]+1]="S"
        A[sP[0]] = "".join(orgin)

        sP[1]=sP[1]+1

    #if tP[1]<sP[1] and sP[1]!=0 and A[sP[0]][sP[1]-1]=="T":
    #    result = True
    #    return result

    if tP[1]>sP[1] and sP[1]!=len(A[0])-1 and A[sP[0]][sP[1]+1]!="*":
        origin = list(A[sP[0]])
        origin[sP[1]]="."
        origin[sP[1]+1]="S"
        A[sP[0]]="".join(origin)
        sP[1]=sP[1]+1

        find(A,sP,depth+1,tP, result)
        origin = list(A[sP[0]])
        origin[sP[1]]="."
        origin[sP[1]-1]="S"
        A[sP[0]]="".join(origin)
        sP[1]=sP[1]-1

    # if tP[1]>sP[1] and sP[1]!=len(A[0])-1 and A[sP[0]][sP[1]+1]=="T":
     #   result = True
     #   return result

    if tP[0]<sP[0] and sP[0]!=0 and A[sP[0]-1][sP[1]]!="*":
        first = list(A[sP[0]])
        first[sP[1]]= "."
        A[sP[0]]="".join(first)
        second = list(A[sP[0]-1])
        second[sP[1]]="S"
        A[sP[0]-1]="".join(second)
        sP[0]=sP[0]-1
        find(A,sP,depth+1,tP, result)

        first = list(A[sP[0]])
        first[sP[1]]= "."
        A[sP[0]]="".join(first)
        second = list(A[sP[0]+1])
        second[sP[1]]="S"
        A[sP[0]+1]="".join(second)
        sP[0]=sP[0]+1
   # if tP[0]<sP[0] and sP[1]!=0 and A[sP[0]-1][sP[1]]=="T":
    #    result = True
     #   return result

    if tP[0]>sP[0] and sP[0]!=len(A)-1 and A[sP[0]+1][sP[1]]!="*":
        first = list(A[sP[0]])
        first[sP[1]]= "."
        A[sP[0]]="".join(first)
        second = list(A[sP[0]+1])
        second[sP[1]]="S"
        A[sP[0]+1]="".join(second)
        # A[sP[0]][sP[1]] = "."
        # A[sP[0]+1][sP[1]]="S"
        sP[0]=sP[0]+1
        find(A,sP,depth+1,tP,result)

        first = list(A[sP[0]])
        first[sP[1]]= "."
        A[sP[0]]="".join(first)
        second = list(A[sP[0]-1])
        second[sP[1]]="S"
        A[sP[0]-1]="".join(second)
        sP[0]=sP[0]-1
    #if tP[0]>sP[0] and sP[1]!=0 and A[sP[0]+1][sP[1]]=="T":
    #    result = True
    #    return result

# print(findher(["....*",".....",".....","*S**.","T**.*"]))
print(findher([
    "S..*",
    "*.**",
    "...T"
]))