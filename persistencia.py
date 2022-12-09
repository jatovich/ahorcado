# -*- coding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Tecnologías de la Información y de la Comunicación II - 2º BTO
# IES José Marin - Curso 2022 / 2023

# Módulo de persistencia de datos.

import json

def f_cargar():
    
    f = open("datos.json", "r")
    jugadores = json.load(f)
    f.close()

    return jugadores

def f_guardar(jugadores):

    f = open("datos.json", "w")
    json.dump(jugadores, f)
    f.close()

    return None

