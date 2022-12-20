name = input("please enter your name:  ")
family = input("please enter your family: ")

a = float(input("please enter your score in the first lesson: "))
b =  float(input("please enter your score in the second lesson: "))
c =  float(input("please enter your score in the third lesson: "))

average = (a+b+c)/3

if average >= 17 :
    print("name,family,educational status is Greate")

if 17 > average >=12 :
    print("name,family,educational status is Normal")

if 12 > average :
    print("name,family,educational status is Fail")
    

