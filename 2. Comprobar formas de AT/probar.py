import sys
import glob
import os
from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser

def imprimir_arbol_jerarquico(node, parser, prefijo="", es_ultimo=True):
    """
    Imprime de forma jerárquica el Parse Tree a partir de los nodos de ANTLR.
    """
    conector = "└── " if es_ultimo else "├── "
    
    # Si es nodo terminal (token: '3', '+', '4', '*')
    if isinstance(node, TerminalNodeImpl):
        texto = node.getText().strip()
        print(f"{prefijo}{conector}'{texto}'")
        return

    # Si es regla sintáctica no terminal (expr, term, factor)
    nombre_regla = parser.ruleNames[node.getRuleIndex()]
    print(f"{prefijo}{conector}{nombre_regla}")

    nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
    total_hijos = node.getChildCount()
    for i in range(total_hijos):
        hijo = node.getChild(i)
        es_ultimo_hijo = (i == total_hijos - 1)
        imprimir_arbol_jerarquico(hijo, parser, nuevo_prefijo, es_ultimo_hijo)

def analizar_archivo_txt(ruta_txt):
    """
    Lee una expresión directamente de un archivo .txt usando FileStream de ANTLR
    y muestra el árbol sintáctico directamente desde ANTLR.
    """
    print("\n" + "=" * 70)
    print(f" ARCHIVO DE PRUEBA: {os.path.basename(ruta_txt)}")
    print("=" * 70)

    # 1. Leer el archivo usando FileStream nativo de ANTLR
    input_stream = FileStream(ruta_txt, encoding='utf-8')
    contenido = str(input_stream).strip()
    print(f"Expresión leída: {contenido}")

    # 2. Análisis léxico y sintáctico
    lexer = ExpresionesLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExpresionesParser(tokens)
    tree = parser.expr()

    # 3. Mostrar el árbol DIRECTAMENTE desde ANTLR (Trees.toStringTree)
    print("\n[ÁRBOL DIRECTO DESDE ANTLR (Formato LISP)]:")
    arbol_antlr = Trees.toStringTree(tree, recog=parser)
    print(arbol_antlr)

    # 4. Mostrar la estructura jerárquica (Diapositiva 12)
    print("\n[ESTRUCTURA JERÁRQUICA DEL PARSE TREE (Diapositiva 12)]:")
    imprimir_arbol_jerarquico(tree, parser)
    print("-" * 70)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Si se especifica un archivo por argumento (ej. python probar.py prueba1.txt)
        for arg in sys.argv[1:]:
            if os.path.exists(arg):
                analizar_archivo_txt(arg)
            else:
                print(f"Error: No se encontró el archivo {arg}")
    else:
        # Si no se pasan argumentos, procesa todos los archivos prueba*.txt en orden
        archivos = sorted(glob.glob("prueba*.txt"))
        if not archivos:
            print("No se encontraron archivos prueba*.txt en el directorio actual.")
        else:
            print(f">>> Ejecutando pruebas para {len(archivos)} archivo(s) .txt encontrados:\n")
            for ruta in archivos:
                analizar_archivo_txt(ruta)
