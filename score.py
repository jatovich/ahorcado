# -*- coding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Tecnologías de la Información y de la Comunicación II - 2º BTO
# IES José Marin - Curso 2022 / 2023

# Módulo encargado de gestionar a los jugadores, sus puntuaciones, y el proceso de guardar
# y cargar sus datos en el programa.
from persistencia import f_cargar, f_guardar

def f_sumar_score(jugador):
    '''Funcion que suma puntuacion al jugador en el archivo datos.json'''

    jugadores = f_cargar("datos.json")
    for usuario in jugadores:
        if usuario["nombre"] == jugador["nombre"]: 
            jugadores.remove(usuario)
            usuario["score"] += 1
            jugadores.append(usuario)
    f_guardar("datos.json", jugadores)



