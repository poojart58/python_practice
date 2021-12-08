#If in the string of number passed, there are only even number then the result will be smallest number. If there are odd and even mixed, 
#then it will print highest among all the numbers

def myfunc(*args):
    b=[]
    c=[]
    for a in range(0,len(args),1):
      #collect all the even numbers in a list
        if args[a]%2==0:
            b.append(args[a])
            b.sort()
        else:
       #all odd number in another list
            c.append(args[a])
            c.sort()
      #check if there are any odd numbers in the list
    if len(c)==0:
        print(b[0])
        
    elif b[-1]>c[-1]:
        print(b[0-1])
        
    else:
        print(c[-1])
