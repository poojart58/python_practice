number_occ={}
new_lst=[]
lst=[2,2,2,2,3,3,3,3,4]
for a in lst:
    if a in number_occ:
        number_occ[a]=1+number_occ[a]
    else:
        number_occ[a]=1
for b in number_occ:
    if number_occ[b]==max(number_occ.values()):
        new_lst.append(b)
new_lst
