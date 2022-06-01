import itertools

def performIterator (tuplevalues):
    
    main_list = []
    tuple0, tuple1, tuple2, tuple3= tuplevalues
    n = len(tuple0)
    
    task_1 = []
    iterator_tuple = itertools.cycle(tuple0)
    
    for _ in range(n): task_1.append(next(iterator_tuple))
        
    task_2 = list(itertools.repeat(tuple1[0], n))
    
    def add_num(x, y): return x+y
    
    task_3 = list(itertools.accumulate(tuple2, add_num))
   
    task_4 = list(itertools.chain(tuple0, tuple1, tuple2, tuple3))
    
    task_5 = itertools.filterfalse(lambda x: x % 2==0, tuple(task_4))
    
    main_list.append(tuple(task_1))
    main_list.append(tuple(task_2))
    main_list.append(tuple(task_3))
    main_list.append(tuple(task_4))
    main_list.append(tuple(task_5))
    
    return tuple(main_list)
            
print(performIterator(((1,10,5,2),(8,48,14,63),(59,47,49,22), (19, 60,1,40))))