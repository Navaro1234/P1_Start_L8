from sterren_module import *
import random

kleuren = ("red", "orange", "yellow", "lime green", "orchid", "magenta", "dodger blue", "crimson", "chocolate", "navy", "salmon", "green yellow", "teal", "cyan", "aquamarine", "hot pink", "firebrick", "royal blue", "wheat")

for _ in range(30):
    random_kleuren = random.choice(kleuren)
    random_x = random.randint(-350, 350)
    random_y = random.randint(-300, 300)
    teken_ster(random_x, random_y, random_kleuren)

turtle.exitonclick()