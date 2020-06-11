from Video import Video
class Episodio(Video):
    def __init__(self,iD,nombre,duracion,calificacion,fecha,temporada,episodio):
        super().__init__(iD,nombre,duracion,calificacion,fecha)
        self.tem=temporada
        self.epi=episodio

    def getID(self):
        return self.i_d

    def mostrar_video(self):
        return f' {self.name}    {self.i_d}    {self.calif}    {self.duration}    {self.date}    {self.tem}    {self.epi}'

    def __gt__(self,n):
        return self.calif > n 

    def __eq__(self,nombre):
        if (nombre==self.name):
            return True

    def calificar(self,nombre,nc):
        if (self.name == nombre):
            self.calif=nc

    def __str__(self):
        return f' {self.name}    {self.i_d}    {self.calif}    {self.duration}    {self.date}    {self.tem}    {self.epi}'

if __name__=='__main__':
    e = Episodio('t2343','piloto','1 hr',7,'27/2',1,1)
    print(e.mostrar_video())
    e.calificar('piloto',9)
    print(e>7)
    print(e.mostrar_video())


