def setup():
    size(600, 180)
    smooth()
    background(0)
    noLoop()
    font = loadFont("Candara-Light-48.vlw")
    textFont(font , 48)
    fill(178, 7, 157)
    
def draw():
    text("The world is here ", 120, 100)
