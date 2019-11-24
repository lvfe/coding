def canAttend(intervals):
    if len(intervals)<=1:
        return True
    intervals=sorted(intervals, key=lambda s:s[0])
    # print(intervals)
    for i in range(1,len(intervals)):

        if intervals[i-1][1]>intervals[i][0]:
            return False

    return True



print(canAttend([(8,8),(7,18),(2,1)]))