import sys
import glob
import os
from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser

def imprimir_arbol_sencillo(node, parser, nivel=0):
    espacios = "  " * nivel
    
    if isinstance(node, TerminalNodeImpl):
        texto = node.getText().strip()
        print(f"{espacios}-> {texto}")
        return

    nombre_regla = parser.ruleNames[node.getRuleIndex()]
    print(f"{espacios}* {nombre_regla}")

    for i in range(node.getChildCount()):
        imprimir_arbol_sencillo(node.getChild(i), parser, nivel + 1)

def procesar_archivo(ruta):
    print("\n\n")
    print(os.path.basename(ruta))
    
    input_stream = FileStream(ruta, encoding='utf-8')
    print(str(input_stream).strip())
    print()

    lexer = ExpresionesLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExpresionesParser(tokens)
    
    tree = parser.expr()

    print("arbol antlr:")
    print(Trees.toStringTree(tree, recog=parser))
    print()

    print("arbol en orden decendente:")
    imprimir_arbol_sencillo(tree, parser)
    print("\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            procesar_archivo(arg)
    else:
        archivos = sorted(glob.glob("prueba*.txt"))
        if len(archivos) == 0:
            print("no hay archivos de prueba")
        else:
            for txt in archivos:
                procesar_archivo(txt)
