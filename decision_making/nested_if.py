weather=input()
time_of_day=input()
if weather=="sunny":
    if time_of_day=="day":
        print("go for a walk")
    else:
        print("play indoor games")
elif weather=="rainy":
    if time_of_day=="night":
        print("sleep")
    else:
        print("Eat hot snack items")
else:
    print("play cricket")            
print("xyz")