def setup():
    size(500, 500)
    smooth()
    stroke(100)
    strokeWeight(30)
def draw():
    background(0)
    line(100, 100, 200, 200)
    line(200, 100, 100, 200)
    println(frameCount)
