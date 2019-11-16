def setup():
    background(255)
    size(500, 500)
    smooth()

l1x1 = 0
l1y1 = 0
l1x2 = 500
l1y2 = 500
flug = 1
r = 10
g = 150
b = 100

def draw():
    global l1x1, l1y1, l1x2, l1y2, flug, r, g, b
    background(255)
    strokeWeight(50)
    stroke(r, g ,b , 20)
    line(l1x1, l1y1, l1x2, l1y2)
    for i in range(1, 11):
        k = i*50
        stroke(r, g, b, 20 + i*10)
        line(l1x1 + k, l1y1, l1x2, l1y2 - k)
        line(l1x1, l1y1 + k, l1x2 - k, l1y2)
    if l1x1 == l1x2 or (l1x1 + k) == l1x2 or l1x1 == (l1x2 - k): #условия изменения цвета(центральная линия имеет минимальную длину)
        r = random(0 ,150)
        g = random(0 ,150)
        b = random(0 ,150)
    
    l1x1 += flug
    l1y1 += flug
    l1x2 -= flug
    l1y2 -= flug
    
    if l1y2 < 0 or l1y2 > 500:
        flug = flug*(-1)
