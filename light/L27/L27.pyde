def setup():
    size(500, 500)
    smooth()
def draw():
    if frameCount == 1:
        counter = 0
    global counter
    noStroke()
    fill(10, 50)
    rect(-1, -1, width + 1, height + 1)
    ny = sin(counter)*100 + 200
    nx = counter*10
    stroke(250)
    strokeWeight(20)
    line(nx, ny, nx, ny)
    counter += 0.1
    if nx > width:
        counter = 0
    
