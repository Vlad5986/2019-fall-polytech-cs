def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)
i = 0
k = 1

def upDate():
    global i, k
    i = i + k
    if i == 255:
        k = -1
    if i == 0:
        k = 1

def draw():
    global i
    stroke(i, 20)
    line(0, mouseY - random(-20, 20), 500, mouseY + random(-20, 20))
    upDate()
