def setup():
    size(500, 500)
    smooth()
    background(255)
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
    mRandom = random(-20, 20)
    mY1 = mouseY - mRandom
    mY2 = mouseY + mRandom
    line(0, mY1, 500, mY2)
    upDate()
