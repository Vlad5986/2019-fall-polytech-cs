def setup():
    size(300, 300)
    smooth()
    strokeWeight(30)
    background(0)
i = 0
k = 1
def draw():
    stroke(i, 20)
    line(mouseX - 50, mouseY - 50, mouseX + 50, mouseY + 50)
    line(mouseX + 50, mouseY - 50, mouseX - 50, mouseY + 50)
    global i, k
    i = i + k
    if i == 255:
        k = -1
    if i == 0:
        k = 1
