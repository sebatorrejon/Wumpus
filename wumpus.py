
class Wumpus:
    def __init__(self):
        self.tablero = [["","","",""],["","","",""],["","","",""],["","","",""]]
        self.inicializar_tablero()
        self.feedback()
        

    def inicializar_tablero(self):
        self.tablero[0][0]="C"
        self.tablero[2][0]="P"
        self.tablero[0][2]="W"
        self.tablero[2][2]="P"
        self.tablero[3][3]="P"
        self.tablero[1][2]="G"

    def draw_board (self):
        for i in range (0 , 4):
            for j in range(0 , 4):
                print(f"{self.tablero[i][j]} |", end="   ")
            print()

    def dentro_limites(self,x,y):
        if x < 0 or x > 3 or y < 0 or y > 3:
            return False
        else:
            return True
    def verificacion_adyacente(self,i,j,c):
        # Verificacion arriba
        if self.dentro_limites(i,j-1) == True:
            self.tablero[i][j-1] = self.tablero[i][j-1] + c
        # Verificacion abajo
        if self.dentro_limites(i,j+1) == True:
            self.tablero[i][j+1] = self.tablero[i][j+1] + c 
        # Verificacion derecha
        if self.dentro_limites(i+1,j) == True:
            self.tablero[i+1][j] = self.tablero[i+1][j] + c
        # Verificacion izquierda
        if self.dentro_limites(i-1,j) == True:
            self.tablero[i-1][j] = self.tablero[i-1][j] + c         

    def feedback(self): 
        for i in range (0 ,4): 
            for j in range (0 ,4):
                if self.tablero[i][j]== "W":
                    self.verificacion_adyacente(i,j,"S")
                if self.tablero[i][j]== "P":
                    self.verificacion_adyacente(i,j,"B")    
                    
def main():
    wumpus = Wumpus()
    wumpus.draw_board()

if __name__ == "__main__":
    main()