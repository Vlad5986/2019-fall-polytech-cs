def setup():
    size(500, 500)
    smooth()
    strokeWeight(1)
    background(0)
i = 0
k = 1
flug = 1

def draw():
    global i, k, flug
    stroke(i, 20)
    if flug == 1:
        line(mouseX, mouseY, random(0, 500), 500)
    else:
        line(mouseX, mouseY, 500, random(0, 500))
    i = i + k
    if i == 255:
        k = -1
    if i == 0:
        k = 1
def keyPressed():
    global flug
    if key == 's':
        saveFrame("myProcessing.png")
    if key == 'q':
        flug = flug*(-1)
