number = int(input("Enter a number: "))

if number % 2 != 0 or number % 5 == 0:
    print(f"{number} is odd or divisible by 5.")
else:
    print(f"{number} is neither odd nor divisible by 5.")
