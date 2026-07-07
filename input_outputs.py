
#a=input()
#print(a)

'''
a=input("enter something")
print(type(a))
'''

'''
a=input("Enter value:")
b=int(a)
print(type(b))

--->if we give b value as number the output is int type
otherwise if we give float value or name or any other the output is invalid 
because we are converting a value into int 
'''

"""
a=int(input())
print(a)
"""

'''
a=input("Enter your name:")
b=int(input("Enter your age:"))
print("My name is", a,"\nand my age is",b)
'''

'''
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print(a,b,sep="-")


---> sep seperates a and b value with given sep condition
the output becomes a-b


a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print(a,b,a,b,sep=" hello ")

---> output is a hello b hello a hello b hello



a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print(a,b,a,b,sep=" hello ",end=" end here")


---> output is 3 hello 5 hello 3 hello 5 end here
at last the end condition comes
'''

'''
a=input()
print("Hello,"+a+"!")

-->srt inp and out
'''

'''
a=int(input("enter a number:"))
print("You entered:",a)

--> it prints space after You entered:
like You entered: a
if we use sep condition then space not prints

example:
a=int(input("enter a number:"))
print("You entered:",a,sep="")
'''
'''
a=input()
b=input()
c=input()
sum=a+b+c
print(sum)
--> it prints abc because it is strings
'''


# a=int(input())
# b=int(input())
# c=int(input())
# sum=a+b+c
# print(sum)

# -->it prints sum

'''
# ex:"john",25

a=input("Enter name and age:")
name,age=a.split(",")
print("Name:",name,",Age:",age)
'''

'''
# ex: arithmetic operations for 10,5
a,b=input("Enter a and b values:").split(",")
a=int(a)
b=int(b)
print(a+b,a-b,a*b,a/b)

# and with using split do all operators 
'''

# 
'''
x,y=input("Enter your name and age:").split(",")
print(f"Name:{x},Age:{y}")

if you dont insert f in print statement 
the output becomes Name:{x},Age:{y}

if you insert f then output becomes Name:yash,Age:19 (input given statements after running)
'''

'''
a=int(input())
b=int(input())
print("Sum:",a+b,sep="")
print(f"Sum:{a+b}")

--> the both print statements represents same
'''
