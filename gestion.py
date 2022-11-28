# -*- coding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Tecnologías de la Información y de la Comunicación II - 2º BTO
# IES José Marin - Curso 2022 / 2023

# Módulo de gestión del juego.

from pantallas import f_pantalla_principal, f_error, f_acercade, f_pedir_palabra, \
     f_despedida, f_letras, f_pedir_letra, f_horca, f_ganador, f_perdedor

def f_jugar():
    '''Función que implementa el juego del ahorcado'''
    
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
                        l[p] = letra_candidata
                    p += 1
            
            # Comprobamos si nos han ahorcado o hemos ganado.
            if nerror == 9:
                f_perdedor(palabra)
                break
            elif None not in l:
                f_ganador(palabra)
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
        
        # Acerca de...
        if op == '4':
            f_acercade()
            
        # Jugar.
        if op == '3':
            f_jugar()
             
    else:
        f_error()
    
    return ret    
    
    