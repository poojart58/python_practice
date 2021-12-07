#This function is used to have an output where the index of even number is capital letter and Odd is small letter
def myfunc(str):
    b=[]
    for a in range(0,len(str),1):
        if a%2==0:
            print(str[a].upper(),end='')
        else:
            print(str[a].lower(),end='')
