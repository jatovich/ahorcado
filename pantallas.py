# -*- coding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Tecnologías de la Información y de la Comunicación II - 2º BTO
# IES José Marin - Curso 2022 / 2023

# Módulo de pantallas, peticiones de información y gráficos del juego.

import pwinput

def f_letras(letras):
    '''Función que visualiza las posiciones de las letras'''
    
    cadena = "La palabra contiene las siguientes letras: "
    
    for letra in letras:
    
        if letra is None: 
            cadena += "_ "
        else:
            cadena += "{} ".format(letra.upper())
    
    print(cadena)
    
    return None
    
def f_despedida():
    '''Función que visualiza la despedida del programa'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
   Vuelve pronto!!!
   '''
    
    print(cadena)
    
    return None

def f_acercade():
    '''Función que visualiza el Acerca de... del programa'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
         Juego del Ahorcado
  Programación y Computación - 2º BTO
   IES Mar Serena - Curso 2021 / 2022
   '''
    
    print(cadena)
    f_continuar()
    
    return None

def f_pantalla_principal():
    '''Función que presenta la pantalla principal del programa, y devuelve la opción introducida'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    1) Cargar jugadores.
    2) Crear jugadores.
    3) Jugar!!!
    4) Resultados jugadores
    5) Acerca de...
    0) Salir
    
    ==> '''
    
    ret = input(cadena)
    
    return ret

def f_error():
    '''Función que devuelve un error al introducir un dato'''
        
    cadena = '''
    
    ==> El Ahorcado <== 
    
    ERROR: El dato introducido no es correcto...'''
    
    print(cadena)
    f_continuar()
    
    return None

def f_continuar():
    '''Función que espera a que pulsemos cualquier tecla para continuar'''
    
    cadena = "Pusle cualquier tecla para continuar..."
    
    input(cadena)
    
    return None

def f_pedir_usuario():
    '''Función que pide la inserción de un nombre de usuario, y lo devuelve'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    Nombre del nuevo jugador: '''
    
    ret = input(cadena)
    
    return ret
  
def f_pedir_palabra():
    '''Función que pide la palabra secreta, y la devuelve'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    Palabra: '''
    ret = pwinput.pwinput(prompt=cadena)
    
    return ret  

def f_pedir_letra():
    '''Función que pide la inserción de una letra, y la devuelve'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    Introduce una letra: '''
    
    ret = input(cadena)
    
    return ret
    
def f_pedir_resolver():
    '''Función que pide una palabra para intentar resolver, y la devuelve'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    Introduce la palabra para resolver la partida: '''
    
    ret = input(cadena)
    
    return ret

def f_ganador(palabra):
    cadena = '''
    
    HAS ACERTADO!!!! La palabra secreta es {}
    '''.format(palabra.lower())
    
    print(cadena)
    f_continuar()
    
    return None

def f_perdedor(palabra):
    cadena = '''
    
    HAS PERDIDO!!!! La palabra secreta es {}
    '''.format(palabra.lower())
    
    print(cadena)
    f_continuar()
    
    return None

    
def f_visualizar_score(jugadores):
    '''Función que visualiza el resultado de los jugadores'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    Resultado de los jugadores
    --------------------------
    '''
    
    linea = ""
    for i in jugadores: 
        linea = "{} - Partidas ganadas: {}\n".format(i["nombre"], i["score"])
        cadena += linea
        cadena += "    "
    print(cadena)
    
    return None

def f_horca(opcion):
    '''Función que visualiza la horca, a partir de la opción pasada como parámetro
    Valores de opcion:
    0 : Pinta la base de la horca.
    1 : El caso 0 y pinta el palo vertical.
    2 : El caso 1 y pinta el palo horizontal superior.
    3 : El caso 2 y pinta la cabeza ahoracada.
    4 : El caso 3 y pinta el tronco del ahorcado.
    5 : El caso 4 y pinta el brazo izquierdo.
    6 : El caso 5 y pinta el brazo derecho.
    7 : El caso 6 y pinta la pierna izquieda.
    8 : El caso 7 y pinta la pierna derecha. AHORCADO!!!
    '''
    
    if int(opcion) == 0:
        cadena = '''
        Han puesto el tablón de abajo...
        
        
        
        
        
        ________
        '''
    elif int(opcion) == 1:
        cadena = '''
        Acaban de poner el palo vertical... ándate con ojo...
        
            |
            |
            |
            | 
        ____|____
        '''        
    elif int(opcion) == 2:
        cadena = '''
        ... uff.. el palo de arriba está listo... siente tu muerte...
        
            |----
            |
            |
            | 
        ____|____
        '''        
    elif int(opcion) == 3:
        cadena = '''
        Ostras!!!! tu cabeza pende de un hilo...
        
            |----
            |   *
            |
            | 
        ____|____
        '''        
    elif int(opcion) == 4:
        cadena = '''
        te veo degadito... 
        
            |----
            |   *
            |   |
            | 
        ____|____
        '''        
    elif int(opcion) == 5:
        cadena = '''
        ... el manco de Lepanto... colega... estás fastidiado...
        
            |----
            |   *
            |   |-
            | 
        ____|____
        '''        
    elif int(opcion) == 6:
        cadena = '''
        ¿haciendo palmas? Espabila que vas a perder!!!
        
            |----
            |   *
            |  -|-
            | 
        ____|____
        '''        
    elif int(opcion) == 7:
        cadena = '''
        A la siguiente te vas al paredón....
        
            |----
            |   *
            |  -|- 
            |  /
        ____|____
        '''        
    elif int(opcion) == 8:
        cadena = '''
        ... te han dejado colgado...
        
            |----
            |   *
            |  -|- 
            |  / \ 
        ____|____
        '''        

    print(cadena)
    return None

def f_jugador_existente():
    cadena = '''
    El jugador introducido ya existe
    '''

    print(cadena)

    return None

def f_jugador_eliminado():
    cadena = '''
    El jugador ha sido eliminado correctamente
    '''

    print(cadena)

    return None

def f_pregunta_eliminar():
    cadena = '''
    ¿Quieres eliminar el usuario? (Si/No) ==> '''

    ret = input(cadena)

    return ret

def f_jugador_creado():
    cadena = '''
    El jugador ha sido creado correctamente
    '''

    print(cadena)

    return None

def f_no_accion():
    cadena = '''
    No se ha realizado ninguna accion
    '''

    print(cadena)

    return None

def f_recordar_carga():
    cadena = '''
    Recuerda cargar un jugador antes de jugar
    '''

    print(cadena)

    return None

def f_cargados():
    cadena = '''
    Error, ya hay dos jugadores cargados, ¿quieres deshacer las cargas realizadas anteriormente? Si/No ==> '''

    ret = input(cadena)

    return ret

def f_jugador_cargado():
    cadena = '''
    Jugador cargado correctamente
    '''

    print(cadena)

    return None

def f_error_carga():
    cadena='''
    El jugador introducido ya ha sido cargado
    '''

    print(cadena)

    return None

def f_letra_revelada():
    cadena = '''
    ERROR: Esa letra ya ha sido introducida.
    '''

    print(cadena)

    return None