from Episodios import Episodio
class Serie():
    def __init__(self,i_d,nombre,genero):
        self.nom=nombre
        self.iD=i_d
        self.genero=genero
        self.episodios=[]
    def mostrar_serie(self):
        return f' {self.nom}    {self.iD}    {self.genero}'

    def getID(self):
        return self.iD

    def getName(self):
        return self.nom

    def agregar(self,episodio):
        self.episodios.append(episodio)

    def __gt__(self,n):
        for i in range (len(self.episodios)):
            if (self.episodios[i]>n) == True:
                print(self.episodios[i]) 

    def calificar(self,name,n):
        for i in range(len(self.episodios)):
            self.episodios[i].calificar(name,n)

    def checar_genero(self,gen):
        return gen in self.genero    

    def mostrar_episodios(self):
        for i in range (len(self.episodios)):
            print(self.episodios[i])

    def getNameEpisodio(self):
        nombres=''
        for i in self.episodios:
            nombres+=f'{i.name}\n'
        return nombres

    def getNameCalif(self):
        nombres=''
        for i in self.episodios:
            nombres+=f'{i.name}  {i.calif}\n'
        return nombres

    def __eq__(self,nombre):
        if (nombre==self.nom):
            return True
        else:
            return False

    def __repr__(self):
        return f' {self.nom}    {self.iD}    {self.genero}'

if __name__=='__main__':
    serie=Serie('vikingos','ttg4','Drama')
    print(serie.checar_genero('Drama'))
    print(serie.mostrar_serie())
    e = Episodio('t2343','piloto', 7 ,20,'27/2',1,1)
    e2 = Episodio('t2342','piloto2', 8 , 20,'27/3',1,2)
    serie.agregar(e)
    serie.agregar(e2)
    print(serie.getNameEpisodio())


    


