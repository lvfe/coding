def strStr(source, target):
    # Write your code here
    if source == target or target == '':
        return 0
    for s in range(0,len(source)):
        if source[s]==target[0]:
            step = 0
            # print(step)
            while step<len(target) and s+step<len(source) and source[s+step] == target[step]:
                # print(step)
                step=step+1
            if step==len(target):
                return s
    return -1
print(strStr("source","rced"))