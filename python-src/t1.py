import turtle


l_system_rules = {'X':'X+YF+', 'Y':'-FX-Y', '+':'+', '-':'-'}
l_system_length = 10
l_system_angle = 90
l_system_iterations = 11
l_system_string = 'FX'
l_system_colours = ["red", "green", "blue", "yellow", "cyan",
                   "magenta", "white", "black", "gray", "gold"]

for i in range(10):
    l_system_rules[str(i)] = str(i)

def draw():
    turtle.setup(800, 600)
    turtle.up()
    turtle.goto(100, -150)
    turtle.down()
    for char in l_system_string:
        if char == 'F':
            turtle.forward(l_system_length)
        elif char == '+':
            turtle.left(l_system_angle)
        elif char == '-':
            turtle.right(l_system_angle)
        else:
            turtle.pencolor(l_system_colours[int(char)])

for _ in range(l_system_iterations):
    result = ''
    for char in l_system_string:
        result += l_system_rules[char]
    l_system_string = result
