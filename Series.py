from Episodios import Episodio
class Serie():
    def __init__(self,nombre,i_d,genero):
        self.nom=nombre
        self.iD=i_d
        self.gen=genero
        self.episodios=[]
    def mostrar_serie(self):
        return f'la serie se llama: {self.nom}, su ID es {self.iD} y su genero es {self.gen}'
    def agregar(self,episodio):
        self.episodios.append(episodio)
    def __gt__(self,n):
        for i in range (len(self.episodios)):
            if (self.episodios[i]>n) == True:
                print(self.episodios[i])                 
    def calificar(self,name,n):
        for i in range(len(self.episodios)):
            self.episodios[i].calificar(name,n)

    def mostrar_episodios(self):
        for i in range (len(self.episodios)):
            print(self.episodios[i])
                 
if __name__=='__main__':
    serie=Serie('vikingos','ttg4','Drama')
    print(serie.mostrar_serie())
    e = Episodio('piloto','t2343', 7 ,20,'27/2',1,1)
    e2 = Episodio('piloto2','t2342', 8 , 20,'27/3',1,2)
    serie.agregar(e)
    serie.agregar(e2)
    serie>8
    serie.mostrar_episodios()


