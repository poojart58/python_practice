def prime_list(num):
    ls=[2]
    for fin in range(3,num+1,2):
        prime = None
        for fin2 in range(2,fin,1):
            if fin%fin2==0 and fin!=fin2:
                prime=False
                break
            if fin%fin2!=0:
                prime=True
                continue
        if prime==True:
            ls.append(fin)
    print(ls)
