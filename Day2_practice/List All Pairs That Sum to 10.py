# From a list, print all unique pairs of numbers whose sum is 10.

arr = [1, 3, 7, 5, 5, 2, 8]
pairs=set()
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j])==10:
            pair = tuple((arr[i], arr[j]))
            if pair not in pairs:
                pairs.add(pair)
print(f"Pairs is {pairs}")