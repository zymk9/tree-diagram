'''
NAME:   HU Benran
STU ID: 20678475
ITSC:   bhuai
'''
import turtle


lsystem_rules   = []
lsystem_length  = 0
lsystem_angle   = 0
lsystem_iterations = 0
lsystem_string  = ''
lsystem_colours = []
starting_position = (0, 0)
starting_angle  = 0
stack = []


def draw():
    turtle.setup(800, 600)
    turtle.up()
    turtle.goto(starting_position)
    turtle.setheading(starting_angle)
    turtle.down()
    for letter in lsystem_string:
        if letter in ['A', 'B', 'C', 'D', 'E', 'F']:
            turtle.forward(lsystem_length)
        elif letter in ['G', 'H', 'I', 'J', 'K', 'L']:
            turtle.up()
            turtle.forward(lsystem_length)
            turtle.down()
        elif letter in ['M', 'N', 'O', 'P', 'X', 'Y']:
            pass
        elif letter == '[':
            item = [turtle.position(), turtle.heading()]
            stack.append(item)
        elif letter == ']':
            item = stack.pop()
            turtle.up()
            turtle.goto(item[0])
            turtle.setheading(item[1])
            turtle.down()
        elif letter == '+':
            turtle.left(lsystem_angle)
        elif letter == '-':
            turtle.right(lsystem_angle)
        elif letter == '^':
            turtle.left(180)
        else:
            turtle.pencolor(lsystem_colours[int(letter)])


print('Welcome to the L-system image generation program!')
print('\nPlease select from one of the following L-systems:')
print('\n a) Dragon curve                   j) Plant A')
print(' b) Koch triangle (90 degree)      k) Plant B')
print(' c) Koch triangle (75 degree)      l) Plant C')
print(' d) Coloured square                m) Simple square')
print(' e) Rainbow line                   n) Simple triangle')
print(' f) Islands and lakes              o) Fishbone')
print(' g) Sierpinski triangle            p) Tree')
print(' h) 12-point star                  q) Beehive')
print(' i) 3-point star')
choice = input('\nEnter your choice (a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q):')

if choice == 'a':
    lsystem_string = "FX"
    lsystem_rules = [ ["X", "X+YF+"], ["Y", "-FX-Y"] ]
    lsystem_length = 10
    lsystem_angle = 90
    lsystem_iterations = 11
    lsystem_colours = []
    starting_position = (100, -150)
    starting_angle = 0
elif choice == 'b':
    lsystem_string = "F"
    lsystem_rules = [ ["F", "F+F-F-F+F"] ]
    lsystem_length = 10
    lsystem_angle = 90
    lsystem_iterations = 3
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'c':
    lsystem_string = "F"
    lsystem_rules = [ ["F", "F+F-F-F+F"] ]
    lsystem_length = 8
    lsystem_angle = 75
    lsystem_iterations = 3
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'd':
    lsystem_string = "1F+2F+3F+4F"
    lsystem_rules = [ ["F", "FF"] ]
    lsystem_length = 250
    lsystem_angle = 90
    lsystem_iterations = 0
    lsystem_colours = [ "black", "red", "green", "blue", "yellow" ]
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'e':
    lsystem_string = "X"
    lsystem_rules = [ ["X", "X0F"],
        ["0", "1"], ["1", "2"], ["2", "3"], ["3", "4"],
        ["4", "5"], ["5", "6"], ["6", "0"] ]
    lsystem_length = 50
    lsystem_angle = 90
    lsystem_iterations = 7
    lsystem_colours = ["red", "orange", "yellow",
        "green", "lime green", "blue", "purple" ]
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'f':
    lsystem_string = "F+F+F+F"
    lsystem_rules = [
        ["F", "F+H-FF+F+FF+FH+FF-H+FF-F-FF-FH-FFF"],
        ["H", "HHHHHH"] ]
    lsystem_length = 30
    lsystem_angle = 90
    lsystem_iterations = 1
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'g':
    lsystem_string = "A"
    lsystem_rules = [ ["A", "B-A-B"], ["B", "A+B+A"] ]
    lsystem_length = 20
    lsystem_angle = 60
    lsystem_iterations = 4
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'h':
    lsystem_string = "X"
    lsystem_rules = [ ["X", "F^FF^F+X"] ]
    lsystem_length = 250
    lsystem_angle = 30
    lsystem_iterations = 6
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'i':
    lsystem_string = "[F][+F-][++F--]"
    lsystem_rules = [ ["F", "FF"] ]
    lsystem_length = 250
    lsystem_angle = 120
    lsystem_iterations = 0
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'j':
    lsystem_string = "F"
    lsystem_rules = [ ["F", "FF[-F+F][+F-F]"] ]
    lsystem_length = 20
    lsystem_angle = 60
    lsystem_iterations = 3
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'k':
    lsystem_string = "F"
    lsystem_rules = [ ["F", "F[+F]F[-F][F]"] ]
    lsystem_length = 25
    lsystem_angle = 20
    lsystem_iterations = 3
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'l':
    lsystem_string = "X"
    lsystem_rules = [ ["X", "F-[[X]+X]+F[+FX]-X"],
    ["F", "FF"] ]
    lsystem_length = 8
    lsystem_angle = 22.5
    lsystem_iterations = 4
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 0
elif choice == 'm':
    lsystem_string = "F+F+F+F"
    lsystem_rules = [ ["F", "FF"] ]
    lsystem_length = 150
    lsystem_angle = 90
    lsystem_iterations = 0
    lsystem_colours = []
    starting_position = (-75, 100)
    starting_angle = 0
elif choice == 'n':
    lsystem_string = "F+F+F"
    lsystem_rules = [ ["F", "FF"] ]
    lsystem_length = 150
    lsystem_angle = 120
    lsystem_iterations = 0
    lsystem_colours = []
    starting_position = (0, 0)
    starting_angle = 30
elif choice == 'o':
    lsystem_string = "A++B"
    lsystem_rules = [ ["A", "F-F++F-A"], ["B", "B-F++F-F"], ["F", "FF"] ]
    lsystem_length = 25
    lsystem_angle = 90
    lsystem_iterations = 4
    lsystem_colours = []
    starting_position = (-144, -144)
    starting_angle = 45
elif choice == 'p':
    lsystem_string = "0F[+1A][-1B]"
    lsystem_rules = [ ["A", "+0F[+1A][-1B]-"], ["B", "-0F[+1A][-1B]+"] ]
    lsystem_length = 80
    lsystem_angle = 10
    lsystem_iterations = 4
    lsystem_colours = ["brown", "green"]
    starting_position = (0, -200)
    starting_angle = 90
elif choice == 'q':
    lsystem_string = "0F"
    lsystem_rules = [ ["F", "+0F-1F-G[-1F-0F]+"], ["G", "GG"] ]
    lsystem_length = 20
    lsystem_angle = 60
    lsystem_iterations = 4
    lsystem_colours = [ "yellow", "gold" ]
    starting_position = (-150, -50)
    starting_angle = 30

print('How many iterations do you want to run?')
iterations = input("Enter '-' if you want to use the default number of iterations:")

if iterations != '-':
    lsystem_iterations = int(iterations)

print('What do you want to do with the L-system?')
print('\n 1) Print the final L-system string')
print(' 2) Display the L-system image in the turtle window')
display_method = input('\nEnter your choice (1/2):')

for _ in range(lsystem_iterations):
    result = ''
    for letter in lsystem_string:
        flag = 0
        for rule in lsystem_rules:
            if letter == rule[0]:
                result += rule[1]
                flag = 1
                break
        if flag == 0:
            result += letter
    lsystem_string = result

if display_method == '1':
    print(lsystem_string)
else:
    turtle.hideturtle()
    turtle.tracer(False)
    draw()
    turtle.update()
