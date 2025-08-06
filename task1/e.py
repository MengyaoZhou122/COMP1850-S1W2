celsius =  float(input("Enter temperature in Celsius: "))

if -100 <= celsius <= 100:
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit:.2f}.")
else:
    print("Temperature out of range.")
