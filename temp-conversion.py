unit=input("select the temperature ('c' for Celsius or 'f' for Fahrenheit.(c/f): ").lower()
temp=float(input("enter the temperature: "))
if unit=="c":
    temp=round((9*temp)/5+32,1)
    print(f"temperature is {temp} °F")
elif unit=="f":
    temp=round((temp-32)*5/9,1)
    
    print(f"temperature is {temp} °C")
else:
    print("Invalid unit. Please enter 'c' for Celsius or 'f' for Fahrenheit.")