number = 10
# - Check if a number is even or odd.
if number % 2 == 0:
    print("even")
else:
    print("odd")

# - Check if a number is positive, negative, or zero.
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

year = 2004
# - Check if a year is a leap year.
if year % 4 == 0:
    print("leap year")
else:
    print("not leap year")

# - Check if a number is prime.

if number > 1:
    for i in range(2, (number//2)+1):
        if (number % i) == 0:
            print("not a prime number")
            break
    else:
        print("prime number")
else:
    print("not a prime number")