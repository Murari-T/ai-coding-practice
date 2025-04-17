def max_element(lst):
    max_ele=lst[0]
    for i in lst:
        if i>max_ele:
            max_ele=i
    return max_ele
    
lst=[10,50,20,90,30]
print(f"Maximun Emement is {max_element(lst)}")