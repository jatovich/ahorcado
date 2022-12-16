#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Tecnologías de la Información y de la Comunicación II - 2º BTO
# IES José Marin - Curso 2022 / 2023

# Módulo de inicio del juego.

from gestion import f_gestion
from persistencia import f_guardar

def main():
    while True: 
        if not f_gestion(): f_guardar("jugadores_cargados.json", []); break
    
if __name__ == '__main__':
    main()
