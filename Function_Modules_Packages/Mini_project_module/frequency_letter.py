def frequency(name):
    dic={}
    for i in name:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    return dic
