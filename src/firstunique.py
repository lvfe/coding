def firstuniq(str):
    list={}
    for i in str:
        if i in list.keys():
            continue
        if str.count(i)==1:
            return i
        else:
            list[i] = str.count(i)
    # timeout
# def fist(str):
    # for i in range(ord('a'), ord('z') + 1):


print(firstuniq("abcdab"))