u=int(input("plese enter your unit you consiumed :"))

if (u<50):
    a=u * 2.60
    sg=25
elif (u<=100):
    a= 130 +((u-50)* 3.25)
    sg=35
elif (u<=200):   
    a=130 +162.50+((u-100)*5.26)
    sg=45
else:
    a=130 +162.50+526+((u-200)*58.45)
    sg=75

ta=a+sg
t=a+sg

print("\nelectricity bill=%.2f" %t)