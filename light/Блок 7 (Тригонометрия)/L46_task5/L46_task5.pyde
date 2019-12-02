counter = 0
counter1 = 0
cx = 250
cy = 250
cRad = 10

def setup():
    size(500, 500)
    smooth()
    background(255)
    strokeWeight(1)

def draw():
    global counter1, cx, cy, cRad, counter
    stroke(0, 50)
    nx = sin(counter1)*cRad + cx
    ny = cos(counter1)*cRad + cy
    x1 = nx - sin(counter)*20
    y1 = ny - cos(counter)*20
    x2 = (nx + sin(counter)*20)*0.125
    y2 = (ny + cos(counter)*20)*0.125
    fill(random(0,255),random(0,255),random(0,255),random(0,100))
    ellipse(x1, y1, x2, y2)
    
    counter += 0.1
    if counter > 2*PI:
        counter = 0
    counter1 += mouseX/float(width*2)
    cRad += mouseX/float(width*2)
    if counter1 > 2*PI:
        counter1 = 0
