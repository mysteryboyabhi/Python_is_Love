def fib(n):
    myarr=[]
    for i in range(n+1):
        myarr.append(i)
    myarr[0] = 0
    myarr[1] = 1
    for j in range(2,n+1):
        myarr[j] = myarr[j - 1] + myarr[j - 2]
    return myarr


print(fib(50))