num = 60
mx = [i for i in range(1, 11)]*6
my = [i for i in range(1, 11)]*6

def setup():
    size(640, 360)
    noStroke()
    fill(255,153)
    
def draw():
    background(51)
    which = frameCount % num
    mx[which] = mouseX
    my[which] = mouseY
    
    for i in range(0, num):
        index = (which +1 +i) % num
        ellipse(mx[index], my[index], i, i)
    
    print(frameCount)
