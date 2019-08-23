n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
cf=[]
minimum=min(n1,n2)
for item in range(1,minimum+1):
    if (n1%item==0) and (n2%item==0):
        cf.append(item)

print(max(cf))
