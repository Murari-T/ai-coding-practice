# You're building a basic AI sensor data preprocessor.
# Given a list of raw sensor data (integers), clean the data using the following rules:

# Remove all out-of-range values (<0 or >100)

# Replace missing values (represented as -1) with the average of valid values

# Count how many values are even, odd, and how many were corrected

raw_data = [45, 101, -1, 60, -1, 99, -10, 34]
#check valid data
valid_data=[x for x in raw_data if 0<=x<=100]
#replace -1 with average of valid_data
average=sum(valid_data)/len(valid_data)
count=0
clean_data=[]
for i in raw_data:
    if i==-1:
        clean_data.append(round(average))
        count+=1
    elif 0<=i<=100:
        clean_data.append(i)
#even count
even_count=sum(1 for j in clean_data if j%2==0)
#odd count 
odd_count=sum(1 for j in clean_data if j%2!=0)

print(f"Valid data is {valid_data}")
print(f"Average {average}")
print(f"Data clean is {clean_data}")
print(f"Replaced values {count}")
print(f"Even count {even_count}")
print(f"Odd count {odd_count}")