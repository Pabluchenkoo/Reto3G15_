"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# ----------------------------------------------------- 


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los avistamientos
    Se crean indices (Maps) por los siguientes criterios:
    -Ciudad
    -Duración
    -Fecha
    -Creo que me hace falta latitud y longitud pero not sure....
    Retorna el analizador inicializado.
    """
    analyzer = {'avistamientos': None,
                'ciudad': None,
                'duracion': None,
                'fecha': None
                }

    analyzer['avistamientos'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['ciudad'] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates)
    analyzer['duracion'] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates)
    analyzer['fecha'] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates)                                    
    # analyzer['ciudad'] = om.newMap(omaptype='BST',
    #                                   comparefunction=compareDates)
    return analyzer
# Construccion de modelos

# Funciones para agregar informacion al catalogo

def addAvistamiento(analyzer, avistamiento):
    """
    """
    lt.addLast(analyzer['avistamientos'], avistamiento)
    updateCiudad(analyzer['ciudad'], avistamiento)
    updateDuracion(analyzer['duracion'], avistamiento)
    updateFecha(analyzer['fecha'], avistamiento)
    return analyzer

def updateCiudad(map, avistamientos):
    """
    Se toma la ciudad del avistamiento y se busca si ya existe en el arbol
    dicha ciudad.  Si es asi, se adiciona a su lista de avistamientos
    y se actualiza el indice de tipos de avistamiento.

    Si no se encuentra creado un nodo para esa ciudad en el arbol
    se crea y se actualiza el indice de tipos de avistamiento
    """
   

def updateDuracion(map, avistamientos):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    

def updateFecha(map, avistamientos):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = avistamientos['datetime']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, crimedate.date())
    if entry is None:
        datentry = newDataEntry(avistamientos)
        om.put(map, crimedate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, avistamientos)
    return map

def addDateIndex(datentry, crime):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstcrimes']
    lt.addLast(lst, crime)
    offenseIndex = datentry['offenseIndex']
    offentry = m.get(offenseIndex, crime['OFFENSE_CODE_GROUP'])
    if (offentry is None):
        entry = newOffenseEntry(crime['OFFENSE_CODE_GROUP'], crime)
        lt.addLast(entry['lstoffenses'], crime)
        m.put(offenseIndex, crime['OFFENSE_CODE_GROUP'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstoffenses'], crime)
    return datentry

def newDataEntry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'offenseIndex': None, 'lstcrimes': None}
    entry['offenseIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareOffenses)
    entry['lstcrimes'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry





# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1