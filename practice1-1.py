import math
 

x = int(input("please choose which operation ? operation with 1 input or 2 inputs? "))


if x == 1 :

   c = float(input("please enter the number: "))
   op = input("please enter operation:  ")


   if op == "sin":
     result = math.sin(math.radians(c))
   if op == "cos":
     result = math.cos(math.radians(c))
   if op == "tan":
     result = math.tan(math.radians(c))
   if op == "cot":
     result = math.cot(math.radians(c))
   if op == "factorial":
     c = int(c)
     result = math.factorial(c)
   if op == "radical":
     result = math.sqrt(c)


if x == 2 :

    a = float(input("please enter the number: "))
    b = float(input("please enter the number: "))
    op = input("plrase enter operation:  ")

    if op == "+":
        result = (a+b)
    if op == "-":
        result = (a-b)
    if op == "*":
        result = (a*b)
    if op == "/":
        result = (a/b)

print(result)
