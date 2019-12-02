def setup():
    size(500, 500)
    smooth()
    background(50)
    strokeWeight(5)
    stroke(250)
    noLoop()

cx = 250
cy = 250
cRad = 200

def draw():
    i = 0
    while i >= 0 and i <= 2*PI:
        i += PI/6
        x1 = cos(i)*cRad + cx
        y1 = sin(i)*cRad + cy
        line(x1, y1, x1, y1)
    line(cx, cy, cx, cy)
    
def keyPressed():
    if key == 's':
        saveFrame("myProcessing.png")
