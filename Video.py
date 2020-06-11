from abc import ABC, abstractmethod
class Video(ABC):
    def __init__(self,iD,nombre,duracion,calificacion,fecha):
        self.name=nombre
        self.i_d=iD
        self.calif=calificacion
        self.duration=duracion
        self.date=fecha

    @abstractmethod    
    def mostrar_video(self):
        pass

    def __gt__(self,n):
        return self.calif > n 

    def calificar(self,nombre,nc):
        if (self.name == nombre):
            self.calif=nc

'''if __name__=='__main__':
    video=Video('star wars','ttg4',8, 26,'27-03')
    video.mostrar_video()
    video.calificar('star wars',9)
    print(video>8)
    video.mostrar_video() #para probarla comenta el @abstractmethod '''
