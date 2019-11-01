def setup():
    size(500, 500)
    background(255)
    noStroke()
def draw():
    for i in range(10):
        for k in range(0, 9, 2):  #добавляет линии где первый квадрат черный(с 1 по 9 с шагом 2)
            fill(i*20)           
            rect(i*40 + 50, 60 + 40*k, 35, 35)
        for j in range(1, 10, 2): #добавляет линии где первый квадрат белый(с 2 по 10 с шагом 2)
            fill(180 - i*20)      #цвет изменяется от белого к черному
            rect(i*40 + 50, 60 + 40*j, 35, 35)
