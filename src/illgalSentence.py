def illgalSentence(str):
    tag = True
    count=0
    list=str.split( )
    for s in list:
        # print(s)
        # print(tag)
        # print(count)
        if tag==True:
            if s[0].islower()==True:
                count=count+1
        tag = False
        # judge others are lower
        for letter in s[1:]:
            if letter.isupper() == True:
                count=count+1
        if s[-1]=='.':
            tag = True
    return count

illgalSentence("This won iz correkt. It has, No Mistakes et Oll. But there are two BIG mistakes in this sentence. and here is one more.")