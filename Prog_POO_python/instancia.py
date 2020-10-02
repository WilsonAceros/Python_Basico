class  Coordenada:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distancia(self, otra_coord):
        x_diff=(self.x-otra_coord.x)**2
        y_diff=(self.y-otra_coord.y)**2
        
        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord1=Coordenada(3,30)
    coord2=Coordenada(4,8)
    
    print(coord1.distancia(coord2))
    print(isinstance(3, Coordenada))