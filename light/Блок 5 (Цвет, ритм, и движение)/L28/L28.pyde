def setup():
    size(500, 500)
    background(0)
def draw():
    colorMode(HSB, width, height, 100)
    stepX = mouseX + 2
    stepY = mouseY + 2
    for gridY in range(0, 500, stepY):
        for gridX in range(0, 500, stepX):
            stroke(gridX, height - gridY, 100)
            strokeWeight(stepX)
            line(gridX, gridY, stepX + gridX, stepY + gridY)
