from Video import Video
class Pelicula(Video):
    def __init__(self,nombre,iD,calificacion,duracion,fecha,gen):
         super().__init__(nombre,iD,calificacion,duracion,fecha)
         self.genero=gen
        
    def mostrar_video(self,num,g):
        if (self.calif > num) or (self.genero == g):
            print (self.name)
        
    def calificar(self,nombre,nc):
        nueva_calif=nc
        return f' la nueva calificacion de {self.name} es: {nueva_calif}'

v = Pelicula ('lola','t2344', 8,'1 hr','27/2','Drama')
v.mostrar_video(10,'Drama')
print(v.calificar('lola',7))

