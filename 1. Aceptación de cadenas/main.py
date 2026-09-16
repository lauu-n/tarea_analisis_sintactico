import os
import sys
from antlr4 import *
from expresiones_aritmeticasLexer import expresiones_aritmeticasLexer
from expresiones_aritmeticasParser import expresiones_aritmeticasParser

def archivo_real(nombre_archivo="ejemplos.txt"):
    if not os.path.exists(nombre_archivo):
        print(f"Archivo no existe :(")
        return

    print(f"~ Evaluando expresiones ~ \n")
    
    # Leer el archivo línea por línea
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # strip elimina espacios en blanco y saltos
            cadena = linea.strip()
            
            # Saltarse líneas vacías en el archivo de texto
            if not cadena:
                continue
                
            # Configurar ANTLR para la línea actual
            input_stream = InputStream(cadena)
            lexer = expresiones_aritmeticasLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = expresiones_aritmeticasParser(stream)

            # Parser desde tu regla inicial
            tree = parser.e()

            # Errores de sintaxis
            if parser.getNumberOfSyntaxErrors() == 0:
                print(f"Cadena aceptada :) \n '{cadena}'")
                print(f"Arbol: {tree.toStringTree(recog=parser)}\n")
            else:
                print(f"Cadena rechazada :( \n '{cadena}'\n")

if __name__ == '__main__':
    # Corrección: Extraer correctamente el string con la ruta del archivo
    if len(sys.argv) > 1:
        archivo_real(sys.argv[1])  # Tomamos el índice [1] que contiene el nombre del archivo
    else:
        archivo_real("ejemplos.txt") # Si no escribes nada, busca ejemplos.txt
