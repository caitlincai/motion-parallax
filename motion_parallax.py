from graphics import graphics
import random

# global variables for mouse position
mouse_x = 0
mouse_y = 0

# draw sky on plain canvas
def create_canvas():
    canvas = graphics(800, 800, "Motion Parallax")
    canvas.rectangle(0, 0, 800, 800, fill="skyblue")
    return canvas

# sun + movement
def draw_sun(canvas, offset_x, offset_y):
    canvas.ellipse(400 + offset_x * 0.1, 100 + offset_y * 0.1, 100, 100, fill="yellow")

def draw_mountains(canvas, colors, offset_x, offset_y):
    # bottom layer mountains, move the slowest
    canvas.triangle(350 + offset_x * 0.5, 800 - (200 + offset_y * 0.3),
                    450 + offset_x * 0.5, 800 - (500 + offset_y * 0.3),
                    600 + offset_x * 0.5, 800 - (200 + offset_y * 0.3),
                    fill=colors[1])

    # middle layer mountains, move at moderate speed
    canvas.triangle(0 + offset_x * 0.7, 800 - (200 + offset_y * 0.1),
                    200 + offset_x * 0.7, 800 - (500 + offset_y * 0.1),
                    450 + offset_x * 0.7, 800 - (200 + offset_y * 0.1),
                    fill=colors[0])

    # top layer mountains, move fastest
    canvas.triangle(400 + offset_x * 0.9, 800 - (200 + offset_y * 0.5),
                    650 + offset_x * 0.9, 800 - (500 + offset_y * 0.5),
                    900 + offset_x * 0.9, 800 - (200 + offset_y * 0.5),
                    fill=colors[2])

def draw_grass(canvas, offset_x, offset_y):
    length = 570 + offset_y
    canvas.rectangle(0, 580 + offset_y, 800, 800, fill="green")

    # vertical lines for grass + movement
    for x in range(0, 800, 10):
        canvas.line(x + offset_x * 0.5, length,
                    x + offset_x * 0.5, length + 40,
                    fill="lime", width=3)

def draw_tree(canvas, offset_x, offset_y):
    # tree trunk
    trunk_x = 500 + offset_x
    trunk_y = 550 + offset_y

    # draw tree trunk
    canvas.rectangle(trunk_x, trunk_y, 20, 100, fill="brown")

    # leaves above trunk
    leaves_x = trunk_x + 10
    leaves_y = trunk_y - 50

    # draw leaves with ellipse
    canvas.ellipse(leaves_x, leaves_y, 120, 150, fill="green")


def draw_birds(canvas):
    birds = []
    # spread the birds
    for i in range(5):
        bird_x = 100 + i * 150
        bird_y = 100 + random.randint(0, 100)  # randomize the height of birds
        birds.append((bird_x, bird_y))
    return birds


def animate_birds(canvas, birds):
    for i in range(len(birds)):
        x, y = birds[i]
        x = (x + 5) % 800  # birds fly right and wrap around
        birds[i] = (x, y)

        # draw birds using 2 lines in a v shape
        canvas.line(x, y, x - 10, y + 10, fill="black", width=2)  # left wing
        canvas.line(x, y, x - 10, y - 10, fill="black", width=2)  # right wing

def apply_parallax(canvas, mountain_colors):
    offset_x = (mouse_x - 400) / 15  # the parallax effect based on mouse x
    offset_y = (400 - mouse_y) / 15  # the parallax effect based on mouse y

    canvas.clear()
    canvas.rectangle(0, 0, 800, 800, fill="skyblue")
    draw_sun(canvas, offset_x, offset_y)
    draw_mountains(canvas, mountain_colors, offset_x, offset_y)
    draw_grass(canvas, offset_x, offset_y)
    draw_tree(canvas, offset_x, offset_y)

def update_mouse_position(event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y

def main():
    canvas = create_canvas()
    birds = draw_birds(canvas)

    # randomize color of mountains
    mountain_colors = [
        canvas.get_color_string(random.randint(50, 200),
                                random.randint(50, 200),
                                random.randint(50, 200))
        for i in range(3)
    ]

    canvas.canvas.bind('<Motion>', update_mouse_position)

    while True:
        apply_parallax(canvas, mountain_colors)
        animate_birds(canvas, birds)
        canvas.update_frame(25)

main()