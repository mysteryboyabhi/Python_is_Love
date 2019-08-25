def fib(n):
    t1=0
    t2=1
    next=0
    for i in range(1,n+1):
        next=t1+t2
        t1=t2
        t2=next
    return t1
def prime(n):
    prime_list=[2]
    num=3
    while len(prime_list)<n:
        for i in prime_list:
            if num%i==0:
                break
        else:
            prime_list.append(num)
        num+=2
    return prime_list[-1]


number=int(input('enter the number'))
if number%2==0:
    print(prime(number//2))
else:
    print(fib(number//2+1))