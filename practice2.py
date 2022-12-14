print("please enter three number for sides of triangle")

a = float(input("please enter first side:  "))
b = float(input("please enter second side: "))
c = float(input("please enter third side:  "))


if a < b + c and  b < a + c and c < a + b :
     print("correct")

else: 
    print("invalid")