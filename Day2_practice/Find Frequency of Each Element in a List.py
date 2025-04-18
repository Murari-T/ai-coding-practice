# Find Frequency of Each Element in a List

lst=[1,2,1,2,4,5,6,5,6,9,9,9]
data=[]
for i in lst:
    if i not in data:
        data.append(i)
for i in sorted(data):
    sum=lst.count(i)
    print(f"Count of {i} is {sum}")