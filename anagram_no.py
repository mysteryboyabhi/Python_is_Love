def myfun(str1,str2):
    str1=str1.replace(" ",'')
    str2 = str2.replace(" ", '')
    if len(str1)!=len(str2):
        return False
    for i in str1:
        if i not in str2:
            return False
        else:
            continue
    for j in str2:
        if j not in str1:
            return False
        else:
            continue
    return True
print(myfun('maam',' amma'))






