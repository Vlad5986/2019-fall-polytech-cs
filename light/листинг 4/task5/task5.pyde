windowWidth = 500
windowHeight = 500
ellipseSize = 200

def setup():
    size(windowWidth, windowHeight)
    background(255)
    fill(50, 80)
    stroke(100)
    strokeWeight(3)

def draw():
    ellipse(windowWidth/2, windowHeight/2 - ellipseSize/2,
        ellipseSize , ellipseSize)
    ellipse(windowWidth/2 - ellipseSize/2, windowHeight/2,
        ellipseSize , ellipseSize)
    ellipse(windowWidth/2 + ellipseSize/2, windowHeight/2,
        ellipseSize , ellipseSize)
    ellipse(windowWidth/2, windowHeight/2 + ellipseSize/2,
        ellipseSize , ellipseSize)
