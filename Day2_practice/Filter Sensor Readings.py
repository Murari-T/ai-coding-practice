# You are given a list of temperature readings. Remove all readings below 10°C or above 45°C (invalid readings) using a loop and logical operators.


readings = [12, 48, 9, 30, 50, 25, 6, 42]
vaild_reading=[]
for reading in readings:
    if 10<=reading<=45:
        vaild_reading.append(reading)
print(f"Valid Readings is {vaild_reading}")