# Generated from Expresiones.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,37,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,
        1,27,9,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,2,0,2,0,2,3,0,2,4,
        0,0,37,0,6,1,0,0,0,2,17,1,0,0,0,4,34,1,0,0,0,6,7,6,0,-1,0,7,8,3,
        2,1,0,8,14,1,0,0,0,9,10,10,2,0,0,10,11,5,1,0,0,11,13,3,2,1,0,12,
        9,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,1,1,0,0,0,
        16,14,1,0,0,0,17,18,6,1,-1,0,18,19,3,4,2,0,19,25,1,0,0,0,20,21,10,
        2,0,0,21,22,5,2,0,0,22,24,3,4,2,0,23,20,1,0,0,0,24,27,1,0,0,0,25,
        23,1,0,0,0,25,26,1,0,0,0,26,3,1,0,0,0,27,25,1,0,0,0,28,35,5,5,0,
        0,29,35,5,6,0,0,30,31,5,3,0,0,31,32,3,0,0,0,32,33,5,4,0,0,33,35,
        1,0,0,0,34,28,1,0,0,0,34,29,1,0,0,0,34,30,1,0,0,0,35,5,1,0,0,0,3,
        14,25,34
    ]

class ExpresionesParser ( Parser ):

    grammarFileName = "Expresiones.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUM", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2

    ruleNames =  [ "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    NUM=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ExpresionesParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpresionesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 14
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExpresionesParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 9
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 10
                    self.match(ExpresionesParser.T__0)
                    self.state = 11
                    self.term(0) 
                self.state = 16
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(ExpresionesParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(ExpresionesParser.TermContext,0)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpresionesParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExpresionesParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 20
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 21
                    self.match(ExpresionesParser.T__1)
                    self.state = 22
                    self.factor() 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExpresionesParser.ID, 0)

        def NUM(self):
            return self.getToken(ExpresionesParser.NUM, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ExpresionesParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(ExpresionesParser.ID)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(ExpresionesParser.NUM)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(ExpresionesParser.T__2)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(ExpresionesParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        self._predicates[1] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




