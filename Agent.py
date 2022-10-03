from msilib.schema import SelfReg


class Agent:
    #Direccion en grados, donde 0 = derecha, 90 = arriba, 180 = izquierda, 270 = abajo
    def __init__(self): 
        self.direction = 0
        self.visualDirection = ">"
        self.posX = 0
        self.posY = 0

    def turn_left(self):
        self.direction = self.direction + 90
        if self.direction > 270:
            self.direction = 0
        self.updateVisualization()

    def turn_right(self):
        self.direction = self.direction -90
        if self.direction < 0:
            self.direction = 270
        self.updateVisualization()

    def updateVisualization(self):
        if self.direction == 0:
            self.visualDirection = ">"
        elif self.direction == 90:
            self.visualDirection = "^"
        elif self.direction == 180:
            self.visualDirection = "<"
        elif self.direction == 270:
            self.visualDirection = "v"

    def moveForward(self):
        if self.direction == 90:
            self.posY -= 1
        if self.direction == 0:
            self.posX += 1
        if self.direction == 180:
            self.posX -= 1
        if self.direction == 270:
            self.posY += 1

    

        
    




