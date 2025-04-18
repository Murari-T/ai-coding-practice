nums = [0, -3, 5, -1, 9, 0, -7]
pos,neg,zero=0,0,0
for i in nums:
    if i==0:
        zero+=1
    elif i<0:
        neg+=1
    else:
        pos+=1
print(f"Positive numbers are {pos}\nNegative Numbers are {neg}\nZeros are {zero}")