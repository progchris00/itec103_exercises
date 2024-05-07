# - Convert a string to uppercase.
string = "hello"
print(string.upper())
# - Convert a string to lowercase.
string = "HELLO"
print(string.lower())
# - Remove duplicate characters from a string.
no_dup = ""
for i in string:
    if i not in no_dup:
        no_dup += i
print(no_dup)
# - Find the length of a string.
print(len(string))
# - Check if a string contains only digits.
print("555".isdigit())