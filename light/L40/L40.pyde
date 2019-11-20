def setup():
    size(500, 500)
    smooth()
    background(50)
    strokeWeight(2)
    noLoop()

cx = 250
cy = 250
cRad = 200

def draw():
    i = 0
    while i >= 0 and i <= 2*PI:
        for k in range(255):
            i += 2*PI/255
            x1 = sin(i)*cRad + cx
            y1 = cos(i)*cRad + cy
            stroke(k)
            line(cx, cy, x1, y1)

    
def keyPressed():
    if key == 's':
        saveFrame("myProcessing.png")
