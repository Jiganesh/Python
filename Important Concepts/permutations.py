def permute (array, size):
    if size == 0:
        print(array)
    for i in range (size):
        permute(array,size-1)
        if size&1:
            array[size-1],array[0]=array[0],array[size-1]
        else:
            array[size-1],array[i]=array[i],array[size-1]

permute([1,2,3],3)
