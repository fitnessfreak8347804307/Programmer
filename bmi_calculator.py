name = input("ENTER YOUR NAME PLEASE: ")
weight = int(input("PLEASE ENTER YOUR (KG): "))
height = float(input("PLEASE ENTER YOUR HEIGHT(m): "))

def bmic(name, weight, height):
    bmi = weight/height**2
    print(name)
    print("BMI : ", bmi)
    if bmi < 18:
        print(name + " " + "is unhealthy")
    elif 18 < bmi < 25:
        print(name + " " + "is healthy")
    else:
        print(name + " " + "is overweight")
        
res = bmic(name, weight, height)
