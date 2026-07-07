# input
# a=10
# b=20
# output
# a=20
# b=10
'''
a=10
b=20
temp=a
a=b
b=temp
print(a,b)

# -->a=20 b=10 is output
'''
a=int(input("Give a value:"))
b=int(input("Give b value:"))
temp=a
a=b
b=temp
print(a,b)

