# Generated from Expresiones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionesParser import ExpresionesParser
else:
    from ExpresionesParser import ExpresionesParser

# This class defines a complete listener for a parse tree produced by ExpresionesParser.
class ExpresionesListener(ParseTreeListener):

    # Enter a parse tree produced by ExpresionesParser#expr.
    def enterExpr(self, ctx:ExpresionesParser.ExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#expr.
    def exitExpr(self, ctx:ExpresionesParser.ExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#term.
    def enterTerm(self, ctx:ExpresionesParser.TermContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#term.
    def exitTerm(self, ctx:ExpresionesParser.TermContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#factor.
    def enterFactor(self, ctx:ExpresionesParser.FactorContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#factor.
    def exitFactor(self, ctx:ExpresionesParser.FactorContext):
        pass



del ExpresionesParser