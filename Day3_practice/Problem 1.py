# Function to Check Even or Odd


def evenorodd(number):
    if number%2==0:
        return f"Even Number {number}"
    else:
        return f"Odd Number {number}"

print(f"{evenorodd(number=5)}")
print(f"{evenorodd(number=6)}")