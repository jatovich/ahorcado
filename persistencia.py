# -*- coding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Tecnologías de la Información y de la Comunicación II - 2º BTO
# IES José Marin - Curso 2022 / 2023

# Módulo de persistencia de datos.

import json

def f_cargar(archivo):
    '''Funcion para cargar los datos de un archivo json'''
    
    f = open(archivo, "r")
    jugadores = json.load(f)
    f.close()

    return jugadores

def f_guardar(archivo, jugadores):
    '''Funcion para guardar datos en un archivo json'''

    f = open(archivo, "w")
    json.dump(jugadores, f)
    f.close()

    return None

