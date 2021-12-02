##This code is used to find the number of words used in a file


with open('myf.txt') as read_file:
    file_content=read_file.read().split()
    d={}
    for ls in file_content:
        if ls in d:
            d[ls]=d[ls]+1
        else:
                d[ls]=1
    print(d.items())
    
    
    #Output is : dict_items([('hello', 1), ('this', 2), ('is', 2), ('a', 3), ('new', 1), ('file', 1), ('and', 2), ('its', 1), ('secon', 1), ('line', 1), ('one', 2), ('third', 1)])
