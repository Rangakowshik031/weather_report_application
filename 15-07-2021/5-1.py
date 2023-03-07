import turtle
m=turtle.Turtle()
colors=["red","yellow","green","orange"]
for j in range(4):
    #m.color(random.choice(colors))
    m.color(colors[j])
    for i in range(4):
        m.forward(150)
        m.right(90)
    m.right(18)
