def depulicate(nums):
    tmp=[]
    for i in nums:
        if i in tmp:
            continue
        else:
            tmp.append(i)
    tmpl=len(tmp)
    for i in range(0,len(nums)-len(tmp)):
        tmp.append('?')

    nums=tmp
    return tmpl
print(depulicate([0,30,3,35,3]))