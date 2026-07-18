
# using f-strings

name=input("Enter a name:")
Age=int(input("Enter your age:"))
print(f"My name is {name} and I am {Age} years old")

# using format method ### .format(x,x)

name=input("Enter a name:")
Age=int(input("Enter your age:"))
print("My name is {} and I am {} years old".format(name,Age))

# using % operator (old style)

name=input("Enter a name:")
Age=int(input("Enter your age:"))
print("My name is %s and I am %d years old"%(name,Age))