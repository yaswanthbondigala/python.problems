# String Slicing = division of String into several parts
# String_variable[Start:Stop:Step]
# Start means starting index,stop means ending+1 index,step means increment

name="Yaswanth_Bondigala"
print(name[0:4])                                      
#0 means from starting,4 means (a) but a not not prints, it prints before index of (a) 
# :.it prints Yasw
print(name[2:5])     # it prints swa
print(name[0:8:2])
#  that last 2 is (step) means increment.Increment of 2 means every 2nd digit skips from start index to end index
# :. it prints Ysat
print(name[:3])    # from start to ending before index of stop
# :. it prints Yas
print(name[::2])    # from start to end with skiping every 2nd
# :. Ysat_odgl
print(name[2::])    # from 2nd index to end
print(name[-15:-2])   # -15=3=w,-2=17 but printing till before letter 
# :. wanth_Bondiga
print(name[1::2])    # from 1st index to end by skipping every 2nd
# awnhBniaa
print(name[::-1])   # reverse string   alagidnoB_htnawsaY

# in negative conditions if step value presents slicing moves from right to left
# otherwise left to right

"""
Why does a negative step reverse the direction?

Think of indexes like a road:

0 → 1 → 2 → 3 → 4 → 5 → 6 → 7
+1 means walk forward.
+2 means jump forward two steps.
-1 means walk backward.
-2 means jump backward two steps.

Positive step (+) → ➡️ Move left to right.
Negative step (-) → ⬅️ Move right to left.

"""
