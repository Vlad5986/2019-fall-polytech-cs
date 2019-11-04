def setup():
    size(600, 600)
    smooth()
    strokeWeight(30)
    noLoop()
def draw():
    background(255)
    for i in range(1,8):
        stroke(20*i)
        line(i*50, 200, 150 + (i-1)*50, 300)
        stroke(160 - 20*i)
        line(i*50 + 100, 200, 50 + (i-1)*50, 300)
