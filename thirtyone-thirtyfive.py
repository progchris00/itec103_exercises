import math
import random
# - Check if a string contains only alphabets.
print("string".isalpha())
# - Count the number of words in a string.
string = "Three word sentence."
print(string.count(" ") + string.count("."))
# - Find the factorial of a number.
print(math.factorial(5))
# - Generate a random number.
print(random.randint(0, 5))
# - Generate a random password.
import secrets

password_length = 13
print(secrets.token_urlsafe(password_length))