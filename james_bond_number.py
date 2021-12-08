#to find if the numbers passed in the string contains 007 in same order or not
# 1,2,3,0,4,0,7 -----> True
#7,9,0,0,1 ---> False

def james_bond(*args):
    jb=[]
    for a in args:
        if a in [0,7]:
            jb.append(a)
        else:
            pass
    if jb==[0,0,7]:
        return True
    else:
        return False
