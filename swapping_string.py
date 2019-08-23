a=input('enter first var')
b=input('enter sec var')
print(a,b)
a=a+b
b=a[0:(len(a)-len(b))]
a=a[len(b):]
print(a,b)