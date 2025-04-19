# Function with Default Arguments

def greet(name="user"):
    return f"Hello {name}"

print(f"{greet()}")
print(f"{greet("Learner")}")