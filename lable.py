from turtle import Turtle, colormode
colormode(255)

FONT_NAME = "Courier"
ALIGNMENT = 'center'
FONT = (FONT_NAME, 24, 'normal')

class Lable(Turtle):
    def __init__(self, lable_c, lable_x, lable_y, lable_arg) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(lable_c)
        self.goto(lable_x, lable_y)        
        self.write(arg=lable_arg, align=ALIGNMENT, font=FONT)

    def update(self, new_color):
        self.color(new_color)

    def textUpdate(self, new_text):
        self.clear()
        self.write(arg=new_text, align=ALIGNMENT, font=FONT)