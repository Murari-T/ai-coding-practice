# Remove Duplicates from List (without using set)

lst=[2,5,2,6,8,5,9,4,4,6]
clean_lst=[]
for i in lst:
    if i not in clean_lst:
        clean_lst.append(i)
print(f"Clean list {clean_lst}")