# Alumno : Claudia Sarahi Armenta Maya 
# Matricula : A01378067
import pandas as pd
from Series import Serie
from Episodios import Episodio
from Pelicula import Pelicula
import sys 
# importa la clase que sea el punto de partida de tu solucion
class MiCatalogo:
    def __init__(self):
        self.peliculas=[]
        self.series=[]

    def mostrar_menu(self):
        print (f'     ---- M E N U ----\n1. Cargar archivo de datos\n2. Mostrar los videos en general:\n    1. Una calificación \
mayor a cierto parámtero\n    2. Un cierto género\n3. Mostrar los episodios de una determinada serie \n4. Mostrar las películas con una \
calificacion mayor a cierto número\n5. Calificar un video\n    - Titulo de película o nombre episodio de la serie\n    - Valor otorgado \
\n6. Salir')
        while True:
            try:
                num=int(input('ingresa un numero: '))
                if num < 1 or num > 6:
                    raise Exception
            
            except ValueError:
                print('no es un numero')   
            except Exception:
                print('tiene que ser un numero entre 1 y 6')   
            else: 
                break 
        return num

    def ask4_2(self):
        print('1. calificacion \n2. genero')
        while True:
            try:
                new_num=int(input('ingresa un numero: '))
                if new_num < 1 or new_num  > 2:
                    raise Exception
                
            except ValueError:
                print('tiene que ser un numero entero')   
            except Exception:
                print('tiene que ser entre 1 o 2')   
            else: 
                break 

        return new_num

    def calificacion_video(self):
        cali= float(input('dame una calificacion: '))
        for i in self.peliculas:
            if (i > cali):
                print(i.getNameCalif())
        for j in self.series:
            if (j>cali):
                print(j.getName())

    def genero_video(self):
        genero= input('dame el nombre del genero: ')
        for i in self.peliculas:
            if i.checar_genero(genero):
                print(i.getName())

        for j in self.series:
            if j.checar_genero(genero):
                print(j.getName())
                       
    def start(self):
        while  True:
            num=self.mostrar_menu()
            if num == 1:
                self.abrir()
            elif num ==2:
                newnum=self.ask4_2()
                if newnum == 1:
                    self.calificacion_video()
                else:
                    self.genero_video()
            elif num ==3:  
                self.ask4_3()
            elif num==4:
                self.ask4_4()
            elif num==5:
                self.ask4_5()
            elif num==6:
                sys.exit('adios')

    def ask4_3(self):
        nombre= input('dame el nombre de la serie: ')
        for i in self.series:
            if i == nombre:
                print(i.getNameEpisodio())

    def ask4_4(self):
        cali= float(input('dame una calificacion: '))
        for i in self.peliculas:
            if (i > cali):
                print(i)

    def ask4_5(self):
        nombre= input('dame el nombre del video: ')
        cali= float(input('dame la calificacion que quieres darle: '))
        for i in self.series:
            i.calificar(nombre,cali)
            print(i.getNameCalif())

        for j in self.peliculas:
            j.calificar(nombre,cali)
            print(j.getNameCalif())

    def agregar_series_series(self,otro):
        self.series.append(otro)
    def agregar_peliculas_peliculas(self,otro):
        self.peliculas.append(otro)

    def abrir(self):
        df= pd.read_excel("BasePelículas.xlsx")
        p_df = df.loc[df['Temporada'].isnull()]
        p_df = p_df[['ID','Nombre Pelicula/Serie','Duración','Género','Calificación','Fecha Estreno']]
        p = p_df.values.tolist()
        for i in p:
            self.peliculas.append(Pelicula(*i))

        se_df = df.loc[df['Temporada'].notnull()]
        se_df = se_df[['ID','Nombre Pelicula/Serie','Género']]
        se = se_df.values.tolist()
        series=[]
        for i in se:
            if i not in series:
                series.append(i)
        for j in series:
            self.series.append(Serie(*j))

        ep_df = df.loc[df['Temporada'].notnull()]
        ep_df = ep_df[['ID','Nombre Episodio','Duración','Calificación','Fecha Estreno','Temporada','Num Episodio']]
        ep = ep_df.values.tolist()
        lsobEp = []
        for k in ep:
            lsobEp.append(Episodio(*k))


        for q in self.series:
            for w in lsobEp:
                if q.getID() in w.getID():
                    q.agregar(w)

if __name__ == "__main__":
    streaming = MiCatalogo()
    streaming.start()
   



