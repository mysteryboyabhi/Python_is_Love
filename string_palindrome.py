def is_palindrome(str_1):
    punc=''' ',!,@," "'''
    str_1=str_1.lower()
    for i in str_1:
        if i in punc:
            str_1=str_1.replace(i,'')
    return str_1==str_1[::-1]


name="dammit i'm mad"
print(is_palindrome(name))