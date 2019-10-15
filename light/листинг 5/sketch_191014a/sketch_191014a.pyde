windowwidth = 500
windowheight = 500
ellipsesize = 100
ellipsewidth = 200
ellipseheight = 300

def setup():
    size(windowwidth, windowheight)
    smooth()
    background(255)
    fill(50, 80)
    stroke(100)
    strokeWeight(3)
    noLoop()
    
def draw():
    ellipse(windowwidth/2, windowheight/2 - ellipsesize/2, ellipsewidth, ellipseheight)
    ellipse(windowwidth/2 - ellipsesize/2, windowheight/2, ellipsewidth, ellipseheight)
    ellipse(windowwidth/2, windowheight/2 + ellipsesize/2, ellipsewidth, ellipseheight)
    ellipse(windowwidth/2 + ellipsesize/2, windowheight/2, ellipsewidth, ellipseheight)
    
