def summer(arr):
    for a in range(0,len(arr)):
        if arr[a]==6:
            val_6=a
        elif arr[a]==9:
            val_9=a+1
        else:
            pass
    del arr[val_6:val_9]
    print(arr)
    print(sum(arr))
    
summer([1,2,6,7,8,9,1,2])
