def setup():
    size(500, 500)
    smooth()
    background(150)
    strokeWeight(1)

flug = 1

def draw():
    fill(flug, 20)
    noStroke()
    mY2 = random(0, 100)
    mX2 = random(0, 100)
    ellipse(mouseX, mouseY, mX2, mY2)

def keyPressed():
    global flug
    if key == 'w':
        flug = 255
    if key == 'b':
        flug = 0
    if key == 's':
        saveFrame('myProcessing.png')
