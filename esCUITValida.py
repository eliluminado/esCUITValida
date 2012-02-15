#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <Aplicacion en Python para verificar la valides de la CUIT.>
# Copyright (C) 2012 Alejandro Alvarez <contacto@codigopython.com.ar>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# http://www.codigopython.com.ar <contacto@codigopython.com.ar>

def esCUITValida(cuit):
    """
    Funcion destinada a la validacion de CUIT
    """
    # Convertimos el valor a una cadena
    cuit = str(cuit)
    # Aca se ve si es de la forma de 13 caracteres
    #   con los guiones
    if len(cuit) == 13 and cuit[2] == '-' and cuit[11] == '-':
        # Removemos los guiones para trabajar
        cuit = cuit.replace('-', '')
    # Si no tiene 11 caracteres lo descartamos
    elif len(cuit) != 11:
        return False, cuit
    # Solo resta analizar si todos los caracteres son numeros
    if not cuit.isdigit():
        return False, cuit
    # Despues de estas validaciones podemos afirmar
    #   que contamos con 11 numeros
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    aux = 0
    for i in xrange(10):
        aux += int(cuit[i]) * base[i]
    aux = 11 - (aux % 11)
    if aux == 11:
        aux = 0
    elif aux == 10:
        aux = 9
    if int(cuit[10]) == aux:
        return True, cuit
    else:
        return False, cuit

if __name__ == "__main__":
    while True:
        print "Para salir ingrese 'Salir'"
        cuit = raw_input('Ingrese la CUIT:\t')
        if cuit == 'Salir' or cuit == 'salir':
            break
        demo = esCUITValida(cuit)
        if not demo[0]:
            print demo[1], "No parece ser un CUIT valido, por favor vuelva a ingresarlo"
        else:
            print demo[1], "Es un numero de CUIT valido"
            break
