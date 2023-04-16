# We need a function count_sel() that receives an array or list of integers (positive and negative) and may give us the following information in the order and structure presented bellow:

# [(1), (2), (3), [[(4)], 5]]

# (1) - Total amount of received integers.

# (2) - Total amount of different values the array has.

# (3) - Total amount of values that occur only once.

# (4) and (5) both in a list

# (4) - It is (or they are) the element(s) that has (or have) the maximum occurrence. If there are more than one, the elements should be sorted (by their value obviously)

# (5) - Maximum occurrence of the integer(s)

def count_sel(lst):
    #A
    #Function that receives a list of integers(pos, neg)
    
    #B
    #total num of ints: length
    t_nums = len(lst)
    print(t_nums)
    #total num of unique ints
    u_nums = len(set(lst))
    print(u_nums)
    #total num of single occurence ints
    num_occur = {}
    s_nums_lst = []
    m_nums_lst = []
    for num in lst:
        if num in num_occur:
            num_occur[num] += 1
        else:
            num_occur[num] = 1
    max_occur = max(num_occur.values())
    print(max_occur)
    
    for num, value in num_occur.items():
        if value == 1:
            s_nums_lst.append(num)
        if max_occur == 1:
            m_nums_lst.append(num)
        elif value == max_occur:
            m_nums_lst.append(num)
            
        
    s_nums = len(s_nums_lst)
    m_nums_lst.sort()
    
     
    #the following will be in a list
    
    # list of the max occuring #s
    #how many times they occur
    
    
    
    return [t_nums, u_nums, s_nums, [m_nums_lst, max_occur]]