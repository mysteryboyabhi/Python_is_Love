n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
def gcd(m,n):
    if n>m:
        (m,n)= (n,m)

    if m%n==0:
        return n
    else:
        return gcd(n,int(m%n))


print(gcd(n1,n2))
