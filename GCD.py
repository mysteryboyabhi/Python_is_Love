n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
fn1=[]
fn2=[]
cf=[]
for i in range(1,n1+1):
    if n1%i==0:
        fn1.append(i)

for j in range(1,n2+1):
    if n2%j==0:
        fn2.append(j)

for item in fn1:
    if item in fn2:
        cf.append(item)

print(max(cf))
