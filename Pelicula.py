from Video import Video
class Pelicula(Video):
    def __init__(self,iD,nombre,duracion,genero,calificacion,fecha):
         super().__init__(iD,nombre,duracion,calificacion,fecha)
         self.genero=genero

    def mostrar_video(self):
        return f'{self.name}    {self.i_d}    {self.calif}   {self.duration}    {self.date}     {self.genero}'

    def __gt__(self,n):
        return self.calif > n 

    def calificar(self,nombre,nc):
        if (self.name == nombre):
            self.calif=nc

    def checar_genero(self,gen):
        return gen in self.genero

    def __repr__(self):
        return f'{self.name}    {self.i_d}    {self.calif}   {self.duration}    {self.date}     {self.genero}'
    def __str__(self):
        return f'{self.name}    {self.i_d}    {self.calif}   {self.duration}    {self.date}     {self.genero}'
    def getName(self):
        return f'{self.name} '
    def getNameCalif(self):
        return f'{self.name}, {self.calif} '

if __name__=='__main__':
    p=Pelicula('tt0107290','Jurassic Park',127,'Action, Adventure, Sci-Fi, Thriller',8.1,'11/6/1993')
    print(p.mostrar_video())
    p.calificar('star wars',9)
    print(p>5)
    print(p.checar_genero('Action'))
    
