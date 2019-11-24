def mostfreq(str):
    result={}
    for i in str:
        if i in result:
            continue
        result[i]=str.count(i)
    list = result.values()
    return max(list)
print(mostfreq("AsssAAA"))
