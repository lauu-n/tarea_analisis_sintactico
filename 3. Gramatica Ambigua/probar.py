from antlr4 import *
from antlr4.error.DiagnosticErrorListener import DiagnosticErrorListener
from antlr4.atn.PredictionMode import PredictionMode

from AmbiguaLexer import AmbiguaLexer
from AmbiguaParser import AmbiguaParser


# ENTRADA QUE VAMOS A PROBAR

entrada = "2 + 3 * 4"


# LEXER

input_stream = InputStream(entrada)

lexer = AmbiguaLexer(input_stream)

tokens = CommonTokenStream(lexer)


# PARSER

parser = AmbiguaParser(tokens)


# DETECCIÓN DE AMBIGÜEDADES

parser.removeErrorListeners()

diagnostico = DiagnosticErrorListener()

parser.addErrorListener(diagnostico)

parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION


# ANALIZAR LA EXPRESIÓN

arbol = parser.expr()


# MOSTRAR ARBOL

print("\nÁrbol generado:")
print(arbol.toStringTree(recog=parser))
