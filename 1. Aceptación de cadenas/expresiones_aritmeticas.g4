grammar expresiones_aritmeticas;

// Sintactico

e : e '+' t
  | t
  ;

t : t '*' f
  | f
  ;

f : ID
  | NUM
  | '(' e ')'
  ;

// Lexico

ID  : [a-zA-Z_] [a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;