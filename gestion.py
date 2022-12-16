# -*- coding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Tecnologías de la Información y de la Comunicación II - 2º BTO
# IES José Marin - Curso 2022 / 2023

# Módulo de gestión del juego.

from persistencia import f_cargar, f_guardar
from pantallas import f_pantalla_principal, f_error, f_acercade, f_pedir_palabra, \
     f_despedida, f_letras, f_pedir_letra, f_horca, f_visualizar_score, f_finalizar, \
     f_letra_revelada, f_pedir_usuario, f_jugador_existente, f_pregunta_eliminar, f_jugador_eliminado, \
     f_continuar, f_no_accion, f_jugador_creado, f_error_cargado, f_recordar_carga, f_jugador_cargado, \
     f_jugador_no_encontrado, f_pedir_resolver, f_posible_palabra, f_rendirse, f_ningun_cargado, f_turno, f_score_sumado
from score import f_sumar_score

def f_crear_jugadores():
    '''Funcion para crear jugadores'''

    jugadores = f_cargar("datos.json")
    nombre_jugador = f_pedir_usuario()
    
    # Revisa en todos los jugadores
    for usuario in jugadores: 
        
        # Si ya existe da la posibilidad de eliminarlo y cierra la funcion
        if usuario["nombre"] == nombre_jugador:
            f_jugador_existente()
            pregunta = f_pregunta_eliminar()
            if pregunta == "Si":
                f_jugador_eliminado()
                jugadores.remove(usuario)
                f_guardar("datos.json",jugadores)
                f_continuar()
                return None
            else: f_no_accion(); f_continuar(); return None
    
    # Añade el jugador a datos.json
    jugador = {"nombre" : nombre_jugador, "score" : 0}
    jugadores.append(jugador)
    f_guardar("datos.json", jugadores)
    f_jugador_creado()
    f_recordar_carga()
    f_continuar()
    return None

def f_cargar_jugador():
    '''Funcion para cargar jugadores dentro del juego'''

    jugadores = f_cargar("datos.json")
    jugadores_cargados = f_cargar("jugadores_cargados.json")
    nombre_jugador = f_pedir_usuario()
    
    # Revisa en ambos archivos json
    for jugador in jugadores_cargados:
        if jugador["nombre"] == nombre_jugador: f_error_cargado(); return None
    for usuario in jugadores:
        
        # Si se encuentra en datos.json lo añade sino marca que no se ha encontrado
        if usuario["nombre"] == nombre_jugador: 
            jugadores_cargados.append(usuario)
            f_guardar("jugadores_cargados.json", jugadores_cargados)
            f_jugador_cargado()
            return None
    f_jugador_no_encontrado()
    f_no_accion()

def f_jugar():
    '''Función que implementa el juego del ahorcado por turnos en funcion de jugadores cargados'''

    # Carga a los jugadores que se han cargado. Sino hay lo recuerda
    jugadores = f_cargar("jugadores_cargados.json")
    if jugadores == []: f_ningun_cargado(); f_recordar_carga(); return None

    # Para cada jugador
    for jugador in jugadores: 
        f_turno(jugador["nombre"])
        
        # Palabra secreta.
        palabra = f_pedir_palabra()
        palabra = palabra.upper()
        nletras = len(palabra)
        
        if nletras > 0:
            
            # Creamos la lista de letras de la palabra secreta.
            l = []
            i = 0
            while i < nletras:
                l.append(None)
                i += 1
        
            nerror = 0
            
            # Visualizamos la palabra.
            f_letras(l)
            

            while True:
                resolver = f_pedir_resolver()
                if resolver in ["Si", "SI", "si", "S", "s"]:
                    palabra_introducida = f_posible_palabra()
                    palabra_introducida = palabra_introducida.upper()
                    if palabra_introducida == palabra: f_finalizar("acertado",palabra);f_sumar_score(jugador);f_score_sumado(); break
                    else: f_horca(nerror); nerror += 1
                
                elif resolver in ["Rendirse", "RENDIRSE", "rendirse", "r", "R"]:f_rendirse(); f_finalizar("perdido", palabra); return None
                
                elif resolver in ["No", "NO", "no", "N", "n"]:
                    # Pedimos letra, y la ponemos en mayúscula.
                    letra_candidata = f_pedir_letra().upper()
                    # Se comprueba si está en la palabra secreta.
                    if not letra_candidata in palabra:
                        f_horca(nerror)
                        nerror += 1
                    else:
                        # Buscamos la letra candidata para ver si existe, y en qué posiciones.
                        p = 0
                        while p < nletras: 
                            if letra_candidata == palabra[p]:
                                # Hay una coincidencia, por lo que lo incluimos...
                                if l[p] == letra_candidata: f_letra_revelada(); break
                                else: l[p] = letra_candidata
                            p += 1
                else: f_error()
                # Comprobamos si nos han ahorcado o hemos ganado.
                if nerror == 9:
                    f_finalizar("perdido",palabra)
                    break
                elif None not in l:
                    f_finalizar("acertado",palabra)
                    
                    # Se le suma score por ganar
                    f_sumar_score(jugador)
                    f_score_sumado()
                    break
                else:
                    f_letras(l)
                
def f_gestion():
    '''Función de gestión del juego'''
    
    ret = True
    
    op = f_pantalla_principal()
    
    if op in ['1','2','3','4','0']:
        
        # Salimos de la aplicación.
        if op == '0':
            f_despedida()
            ret = False
        
        # Cargar jugadores
        if op == "1":
            f_cargar_jugador()

        # Crear jugadores
        if op == "2":
            f_crear_jugadores()

        #Resultados jugadores
        if op == "4":
            jugadores = f_cargar("datos.json")
            f_visualizar_score(jugadores)

        # Acerca de...
        if op == '5':
            f_acercade()
            
        # Jugar.
        if op == '3':
            f_jugar()
             
    else:
        f_error()
    
    return ret    
    
    
