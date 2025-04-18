# Find the Second Largest Number in a List

lst=[1,5,9,6,6,4,9,4,3]
sort_lst=sorted(set(lst))
print(f"Second largest is {sort_lst[-2]}")