def setup():
    size(500, 500)
    smooth()
    strokeWeight(30)
    noLoop()
def draw():
    background(255)
    for i in range(1, 8):
        for k in range(1, 4):
            stroke(20*i)
            line(i*50, 100*k, 150 + (i-1)*50, 100 + 100*k)
            stroke(160 - 20*i)
            line(i*50 + 100, 100*k, 50 + (i - 1)*50, 100 + 100*k)
