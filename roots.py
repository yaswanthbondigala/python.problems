# ex:
# input:
# a=1
# b=-3
# c=2

# output:Roots:(2.0,1.0)

a=int(input("give a value:"))
b=int(input("give b value:"))
c=int(input("give c value:"))

d=b**2-4*a*c
e=(-b+(d**(1/2)))/2*a
f=(-b-(d**(1/2)))/2*a
print(f"Roots:({e},{f})")

# -->for roots -b+or-root b^2-4ac by 2a is formula 
# under root value is wriiten in d and root is converted as power 1 by 2
# and +,- writtened seperately.

# output is Roots:(2.0,1.0)