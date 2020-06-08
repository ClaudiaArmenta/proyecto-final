# Alumno : Claudia Sarahi Armenta Maya 
# Matricula : A01378067

import xlrd
# importa la clase que sea el punto de partida de tu solucion

class MiCatalogo:
    def __init__(self):
        self.peliculas=[]
        self.series=[]
    def mostrar_menu(self):
        while 
    
    def abrir(self):
        filepath="/Users/sara/Documents/GitHub/proyectointegrador-SarahiArmenta/BasePelículas.xlsx"
        workbook=xlrd.open_workbook(filepath)
        sheet=workbook.sheet_by_name('BasePelículas')
        print('no de filas', sheet.nrows)
        print('no de columnas', sheet.ncols)
        for i in range (sheet.nrows):
            if type(sheet.cell_value(i,5)) == float:
                 wrongValue = sheet.cell_value(i,5)
                 workbook_datemode = workbook.datemode
                 y, m, d, h, m, s = xlrd.xldate_as_tuple(wrongValue, workbook_datemode)
                 fecha="{0} - {1} - {2}".format(d, m, y)
            else: 
                fecha=(sheet.cell_value(i,5))
                id_pelicula=(sheet.cell_value(i,0))
                print(fecha)
                print(id_pelicula)
if __name__ == "__main__":
    streaming = MiCatalogo()
    streaming.abrir()
