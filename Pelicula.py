from Video import Video
class Pelicula(Video):
    def __init__(self,nombre,iD,calificacion,duracion,fecha,gen):
         super().__init__(nombre,iD,calificacion,duracion,fecha)
         self.genero=gen

    def mostrar_video(self):
        return f'la pelicula se llama: {self.name},su ID es {self.i_d}, tiene una calificacion de {self.calif}\ndura {self.duration}\
 y se estreno el {self.date}\nsu genero es {self.genero}'

    def __gt__(self,n):
        return self.calif > n 

    def calificar(self,nombre,nc):
        if (self.name == nombre):
            self.calif=nc

    def checar_genero(self,gen):
        return gen in self.genero

    def __str__(self):
        return f'la pelicula se llama: {self.name},su ID es {self.i_d}, tiene una calificacion de {self.calif}\ndura {self.duration}\
 y se estreno el {self.date}\nsu genero es {self.genero}'

        
if __name__=='__main__':
    p=Pelicula('star wars','ttg4',8, 26,'27-03','Si-fi, Romance')
    print(p.mostrar_video())
    p.calificar('star wars',9)
    print(p.checar_genero('Terror'))
