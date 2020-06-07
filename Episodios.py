from Video import Video
class Episodio(Video):
    def __init__(self,nombre,iD,calificacion,duracion,fecha,temporada,episodio):
         super().__init__(nombre,iD,calificacion,duracion,fecha)
         self.tem=temporada
         self.epi=episodio

    def mostrar_video(self,num):
        if (self.calif > num):
            print (self.name)

e = Episodio('piloto','t2343', 90 ,'1 hr','27/2',1,1)
e.mostrar_video(80)

