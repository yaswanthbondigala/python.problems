# String methods are built-in functions in Python that perform different operations on strings,
#  such as changing the case, searching, replacing, splitting, joining,and more

# 1. upper() – Converts all letters to uppercase.
# Input:
text = "python"
print(text.upper())
# Output:
# PYTHON

# --------------------------------------------------

# 2. lower() – Converts all letters to lowercase.
# Input:
text = "PYTHON"
print(text.lower())
# Output:
# python

# --------------------------------------------------

# 3. capitalize() – Converts the first letter to uppercase.
# Input:
text = "python programming"
print(text.capitalize())
# Output:
# Python programming

# --------------------------------------------------

# 4. title() – Converts the first letter of every word to uppercase.
# Input:
text = "python programming"
print(text.title())
# Output:
# Python Programming

# --------------------------------------------------

# 5. strip() – Removes spaces from both the beginning and the end.
# Input:
text = "   Python   "
print(text.strip())
# Output:
# Python

# --------------------------------------------------

# 6. lstrip() – Removes spaces from the beginning (left side).
# Input:
text = "   Python   "
print(text.lstrip())
# Output:
# Python   

# --------------------------------------------------

# 7. rstrip() – Removes spaces from the end (right side).
# Input:
text = "   Python   "
print(text.rstrip())
# Output:
#    Python

# --------------------------------------------------

# 8. replace() – Replaces one word or character with another.
# Input:
text = "I like Java"
print(text.replace("Java", "Python"))
# Output:
# I like Python

# --------------------------------------------------

# 9. split() – Splits a string into a list.
# Input:
text = "Apple,Banana,Mango"
print(text.split(","))
# Output:
# ['Apple', 'Banana', 'Mango']

# --------------------------------------------------

# 10. join() – Joins list elements into one string.
# Input:
fruits = ["Apple", "Banana", "Mango"]
print("-".join(fruits))
# Output:
# Apple-Banana-Mango

# --------------------------------------------------

# 11. find() – Returns the index of the first occurrence.
# Input:
text = "Python"
print(text.find("t"))
# Output:
# 2

# --------------------------------------------------

# 12. index() – Returns the index of a character (gives an error if not found).
# Input:
text = "Python"
print(text.index("h"))
# Output:
# 3

# --------------------------------------------------

# 13. count() – Counts how many times a character appears.
# Input:
text = "banana"
print(text.count("a"))
# Output:
# 3

# --------------------------------------------------

# 14. startswith() – Checks whether the string starts with the given text.
# Input:
text = "Python"
print(text.startswith("Py"))
# Output:
# True

# --------------------------------------------------

# 15. endswith() – Checks whether the string ends with the given text.
# Input:
text = "Python"
print(text.endswith("on"))
# Output:
# True

# --------------------------------------------------

# 16. isalpha() – Returns True if all characters are letters.
# Input:
text = "Python"
print(text.isalpha())
# Output:
# True

# --------------------------------------------------

# 17. isdigit() – Returns True if all characters are digits.
# Input:
text = "12345"
print(text.isdigit())
# Output:
# True

# --------------------------------------------------

# 18. isalnum() – Returns True if all characters are letters or digits.
# Input:
text = "Python123"
print(text.isalnum())
# Output:
# True

# --------------------------------------------------

# 19. isspace() – Returns True if all characters are spaces.
# Input:
text = "   "
print(text.isspace())
# Output:
# True

# --------------------------------------------------

# 20. swapcase() – Changes uppercase to lowercase and lowercase to uppercase.
# Input:
text = "PyThOn"
print(text.swapcase())
# Output:
# pYtHoN