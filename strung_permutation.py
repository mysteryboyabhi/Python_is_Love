def myfun(str_1,str_2):
    str_1=str_1.replace(' ','')
    str_2=str_2.replace(" ",'')
    if len(str_1)!=len(str_2):
        return False
    for char in str_1:
        if char in str_2:
            str_2=str_2.replace(char,'')
    return len(str_2)==0

str_1=input('enter the string first')
str_2=input('enter the string second')
print(myfun(str_1,str_2))
