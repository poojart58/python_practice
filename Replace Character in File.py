#This is a pthon program which replaces a character with another in a file

with open('myf.txt') as File1:
    a=File1.read()
    print(a)
    for i in range(0,len(a),1):
        if a[i]=='i':
            b='I'
            print(b,end='')
        else:
            b=a[i]
            print(b,end='')
