try:
    mylist=[1,2,4,5,5]
    for i in range(4):
        print(mylist[i])
except IndexError as indx:
    print(f"this{indx} ")
else:
    try:
        with open('GC1D.py') as file:
            read=file.read()
            print(read)
    except FileNotFoundError as fnf:
        print(fnf)
    print("you have done ")