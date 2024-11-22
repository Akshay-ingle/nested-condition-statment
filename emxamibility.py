mc=input("if you have any madical cause if yes press Y if no press N :")

an=int(input("enter the attendence first :"))

if mc=="Y":
    print("you are allowed")

else:
    if an>=75:
        print("your are allowed")
    else:
        print("your are not allowed")


        