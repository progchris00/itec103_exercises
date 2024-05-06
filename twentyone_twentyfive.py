term = 5
# - Generate the Fibonacci sequence up to a certain number.
# for i in range(5):

# - Check if a string is a palindrome.
word = "racecar"
if word == word[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# - Count the number of vowels in a string.
vowel_count = 0
vowels = ["a", "e", "i", "o", "u"]
for letter in word:
    if letter in vowels:
        vowel_count += 1
print(vowel_count)

# - Count the number of consonants in a string.
constant_count = 0
for letter in word:
    if letter not in vowels:
        constant_count += 1
print(constant_count)

# - Reverse a string.
print("string"[::-1])