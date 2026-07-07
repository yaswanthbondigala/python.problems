while True:
    print("calculator:")
    print("1.Add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit.")

    choice=input("choose a number(1-5):")
    if choice=="5":
        print("thank you!")
        break
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))


    if choice=="1":
        print("Add=",a+b)
    elif choice=="2":
        print("sub=",a-b)
    elif choice=="3":
        print("mult=",a*b)
    elif choice=="4":
        if b!=0:
            print("div=",a/b)
        else:
            print("not divisible by zero")
    else:
        print("Invalid choice!")            


