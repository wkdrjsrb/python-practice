def set_str(A, B):
    set_A = set(A)
    set_B = set(B)
    
  
    union_set = set_A.union(set_B)           
    intersection_set = set_A.intersection(set_B)  
    difference_set = set_A.difference(set_B)  
    
    print("합집합: ", union_set)
    print("교집합: ", intersection_set)
    print("차집합: ", difference_set)


A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]


set_str(A, B)
