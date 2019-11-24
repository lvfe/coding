import re
def rever(s):
    list = s.split()
    newlist = ''
    for i in range(len(list)-1,-1,-1):
        print(i)
        if i==0:
            newlist = newlist+list[i]
        else:
            newlist = newlist+list[i]+' '
    return newlist
print(rever("how are  you?"))