'''import turtle,random
m=turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue']
def samp(t,s):
    m.color(random.choice(colors))
    for i in range(4):
        t.forward(s)
        t.left(90)

for i in range(1,50):
    m.left(18)
    samp(m,200)'''


import turtle,random
m=turtle.Turtle()
#colors = ['red', 'orange', 'yellow', 'green', 'blue']
def samp(t,s):
    #m.color(random.choice(colors))
    for i in range(4):
        t.forward(s)
        t.left(90)

for i in range(1,100):
    m.left(18)
    samp(m,200)
