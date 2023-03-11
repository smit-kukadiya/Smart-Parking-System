from turtle import Turtle

class Car(Turtle):
    def __init__(self, car_c, c_x, c_y) -> None:
        super().__init__()
        self.penup()
        self.shape(car_c)
        self.goto(c_x, c_y)

    def update(self, car_c):
        self.showturtle()
        self.shape(car_c)

    def clear(self):
        self.hideturtle()