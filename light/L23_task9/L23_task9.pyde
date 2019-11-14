def setup():
    size(500, 500)
    noStroke()
def draw():
    background(255)
    border = 50
    nw = width - 2*border    #ширина сетки
    nh = height - 2*border   #высота сетки
    number = 5               #количество кругов
    nWstep = nw / number     #ширина одной ячейки для круга
    nHstep = nh / number     #высота одной ячейки для круга
    for i in range(number):        #отвечает за смещение по Y
        for j in range(number):    #отвечает за смещение по Х
            x = border + j*nWstep + nWstep/2   #определяет центр каждой ячейки
            y = border + i*nHstep + nHstep/2 
            s = 5 + (4-j + 4-i)*10    #изменили j и i на 4-j и 4 - i тк в массиве range эл-ты от 0 до 4
            mColor = s*1.5
            fill(0, 0, mColor)        #третий аргумент отвечает за синий цвет поэтому изменили его на mColor
            ellipse(x, y, s, s)
            fill(250)
            ellipse(x, y, 3, 3)
            
