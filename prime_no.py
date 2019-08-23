def myfun(num):
    for number in range(2,num):
        if num%number==0:
            print('not prime')
            break
    else:
        print(' prime ')


myfun(20)