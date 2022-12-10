# -*- coding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Tecnologías de la Información y de la Comunicación II - 2º BTO
# IES José Marin - Curso 2022 / 2023

# Módulo encargado de gestionar a los jugadores, sus puntuaciones, y el proceso de guardar
# y cargar sus datos en el programa.
from persistencia import f_cargar, f_guardar
from pantallas import f_pedir_usuario, f_jugador_existente, f_pregunta_eliminar, f_jugador_eliminado, f_jugador_creado, \
     f_no_accion, f_recordar_carga, f_continuar, f_cargados, f_jugador_cargado, f_error_carga

def f_sumar_score(jugador):
    jugadores = f_cargar()
    for usuario in jugadores:
        if usuario["nombre"] == jugador["nombre"]: usuario["score"] += 1
    f_guardar(jugadores)

def f_crear_jugadores():
    jugadores = f_cargar()
    nombre_jugador = f_pedir_usuario()
    for usuario in jugadores: 
        if usuario["nombre"] == nombre_jugador:
            f_jugador_existente()
            pregunta = f_pregunta_eliminar()
            if pregunta == "Si":
                f_jugador_eliminado()
                jugadores.remove(usuario)
                f_guardar(jugadores)
                f_continuar()
                return None
            else: f_no_accion(); f_continuar(); return None
    jugador = {"nombre" : nombre_jugador, "score" : 0}
    jugadores.append(jugador)
    f_guardar(jugadores)
    f_jugador_creado()
    f_recordar_carga()
    f_continuar()
    return None

def f_cargar_jugador():
    global jugador1
    global jugador2
    if jugador1 == None: jugador1 = f_pedir_usuario(); f_jugador_cargado()
    elif jugador2 == None: 
        jugador2 = f_pedir_usuario()
        if jugador2 == jugador1(): f_error_carga(); jugador2 = None
        else: f_jugador_cargado()
    else: 
        pregunta_carga = f_cargados()
        if pregunta_carga == "Si": jugador1 = None; jugador2 = None
        else: f_no_accion()
    
    return None


