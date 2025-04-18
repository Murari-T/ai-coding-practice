# Count Even and Odd Numbers in a List

lst=[1,2,3,4,5,6]
even_count=sum(1 for i in lst if i%2==0)
odd_count=sum(1 for i in lst if i%2!=0)
print(f"Even Sum is {even_count}\nOdd Sum is {odd_count}")