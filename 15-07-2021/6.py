import turtle,random
m=turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue']
for i in range(0,360,36):
    m.color(random.choice(colors))
    m.seth(i)
    m.circle(100)
