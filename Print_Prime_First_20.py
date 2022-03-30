non_prime=[]
prime=[2,3]
i=4

while len(prime)!=20:
    flg=True
    for j in range(2,int(i/2)+1):
        if i%j==0:
            non_prime.append(i)
            flg=False
            break
        else:
            continue
    if flg:
        prime.append(i)
    i=i+1
print(prime)
