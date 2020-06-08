from Video import Video
class Episodio(Video):
    def __init__(self,nombre,iD,calificacion,duracion,fecha,temporada,episodio):
        super().__init__(nombre,iD,calificacion,duracion,fecha)
        self.tem=temporada
        self.epi=episodio

    def mostrar_video(self):
        return f'el episodio se llama: {self.name},su ID es {self.i_d}, tiene una calificacion de {self.calif}\ndura {self.duration}\
 y se estreno el {self.date}\nde la temporada nº {self.tem} y el episodio es el nº {self.epi}'

    def __gt__(self,n):
        return self.calif > n 

    def calificar(self,nombre,nc):
        if (self.name == nombre):
            self.calif=nc

    def __str__(self):
        return f'el episodio se llama: {self.name},su ID es {self.i_d}, tiene una calificacion de {self.calif}\ndura {self.duration}\
 y se estreno el {self.date}\nde la temporada nº {self.tem} y el episodio es el nº {self.epi}'

if __name__=='__main__':
    e = Episodio('piloto','t2343', 7 ,'1 hr','27/2',1,1)
    print(e.mostrar_video())
    e.calificar('piloto',9)
    print(e>7)
    print(e.mostrar_video())


