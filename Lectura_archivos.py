import csv
from Disciplina import Disciplina
from Estado_proyecto import Estado_proyecto
from Funcion import Funcion
from Moneda import Moneda
from Tipo_proyecto import Tipo_proyecto


def leer_archivo(nombre):
    try:
        lista = []
        with open(nombre, 'r', encoding='utf-8') as archivo:  
            lector = csv.reader(archivo)
            cont = 0                 
            for fila in lector: 
                if cont > 0:
                    cadena = '' 
                    for i in fila: 
                        cadena+=i 
                    sublista = cadena.split(';')           
                    lista.append(sublista)
                cont += 1
        return lista
    except FileNotFoundError:
        return
    
def crear_clase_disciplina(lista):
    disciplinas = dict()
    for list in lista:
        dis = Disciplina(list[0],list[1],list[2],list[3],list[4],list[5],list[6])
        disciplinas[list[0]]=dis
    return disciplinas

def crear_clase_estado_proyecto(lista):
    estados_proy = dict()
    for list in lista:
        est = Estado_proyecto(list[0],list[1])
        estados_proy[list[0]]=est
    return estados_proy

def crear_clase_funcion(lista):
    funcion = dict()
    for list in lista:
        fun = Funcion(list[0],list[1])
        funcion[list[0]]=fun
    return funcion

def crear_clase_moneda(lista):
    moneda = dict()
    for list in lista:
        mon = Moneda(list[0],list[1],list[2])
        moneda[list[0]]=mon
    return moneda

def crear_clase_tipo_proyecto(lista):
    tipo_proy = dict()
    for list in lista:
        tipo = Tipo_proyecto(list[0],list[1],list[2],list[3],list[4])
        tipo_proy[list[0]]=tipo
    return tipo_proy

    

