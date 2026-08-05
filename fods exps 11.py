import turtle

t = turtle.Turtle()
t.speed(1)

sales = [15000, 18000, 17000, 22000, 25000, 27000]

t.penup()
t.goto(-250, -150)
t.pendown()
t.forward(500)

t.penup()
t.goto(-250, -150)
t.left(90)
t.pendown()
t.forward(300)

t.penup()
t.goto(-220, -150 + sales[0] / 200)
t.pendown()

x = -220
for s in sales:
    t.goto(x, -150 + s / 200)
    x += 70

turtle.done()
