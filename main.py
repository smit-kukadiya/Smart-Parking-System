from turtle import Screen, ontimer
from lable import Lable
from car import Car
from serialData import serial_data
from time import sleep

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CAR = "s2.gif"
CAR2 = "s.gif"
PARK = "fpark.gif"

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.bgpic("parking.gif")
screen.title("Parking System")
screen.tracer(0)
screen.listen()
screen.register_shape(CAR)
screen.register_shape(CAR2)
screen.register_shape(PARK)
available = 0

#data1 = carlable.carlable(RED, 250, 260, "P1", RED_CAR, 250, 180)
lable1 = Lable("#FFCC00", 600, 300, "Total Parking: 4")
car1 = Car(CAR, 13, 238)
#data2 = carlable.carlable(RED, 0, 260, "P2", RED_CAR, 0, 180)
#lable2 = Lable(RED, 0, 260, "P2")
car2 = Car(CAR, -160, 238)
#data3 = carlable.carlable(RED, -200, 80, "P3", RED_CAR, -200, 0)
#lable3 = Lable(RED, -300, 60, "P3")
car3 = Car(CAR2, -390, 25)
#data4 = carlable.carlable(RED, -200, -140, "P4", RED_CAR, -200, -220)
#lable4 = Lable(RED, -300, -160, "P4")
car4 = Car(CAR2, -390, -150)

lable0 = Lable("#FFCC00", 563, 240, f"Available Parking: {available}")

full_parking = Car(PARK, 0, 0)

while True:

    serial_data()
    available = 0
    first = 1
    file = open("output.txt")
    verylargeData = (file.read()).split("\n")
    largedata = verylargeData[-4:-1]
    list1 = [ele for ele in largedata if ele != '']
    list2 = list1[0].split(" ")
    data = list2[2]
    if data[0] == "0":
        #data1.update(RED, 250, 260, "P1", GREEN_CAR, 250, 180)
        #lable1.update(RED)
        car1.clear()
        if first:
            available += 1
    else:
        #data1.update(GREEN, 250, 260, "P1", RED_CAR, 250, 180)
        #lable1.update(GREEN)
        car1.update(CAR)
        if first != 1:
            available -= 1

    if data[1] == "0":
        #data2.update(RED, 0, 260, "P2", GREEN_CAR, 0, 180)
        #lable2.update(RED)
        car2.clear()      
        if first:  
            available += 1
    else:
        #data2.update(GREEN, 0, 260, "P2", RED_CAR, 0, 180)
        #lable2.update(GREEN)
        car2.update(CAR)
        if first != 1:
            available -= 1
    
    if data[2] == "0":
        #data3.update(RED, -200, 80, "P3", GREEN_CAR, -200, 0)
        #lable3.update(RED)
        car3.clear()
        if first:
            available += 1
    else:
        #data3.update(GREEN, -200, 80, "P3", RED_CAR, -200, 0)
        #lable3.update(GREEN)
        car3.update(CAR2)
        if first != 1:
            available -= 1

    if data[3] == "0":
        #data4.update(RED, -200, -140, "P4", GREEN_CAR, -200, -220)
        #lable4.update(RED)
        car4.clear()
        if first:
            available += 1
    else:
        #data4.update(GREEN, -200, -140, "P4", RED_CAR, -200, -220)
        #lable4.update(GREEN)
        car4.update(CAR2)
        if first != 1:
            available -= 1

        first = 0

    lable0.textUpdate(f"Available Parking: {available}")
    
    if available > 0:
        full_parking.clear()
    else:
        full_parking.update(PARK)

    screen.update()