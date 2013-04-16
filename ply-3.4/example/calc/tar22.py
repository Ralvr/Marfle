import sys

if ".." not in sys.path: sys.path.insert(0, "..")

if sys.version_info[0] < 3:
    input = raw_input

#import ply.lex as lex
reserved = {
	'program'	:	'PROGRAM',
	'variable'		:	'VAR',
	'int'		:	'INT',
	'float'		:	'FLOAT',
	'print'		:	'PRINT',
	'if'		:	'IF',
	'else'		:	'ELSE'
}

tokens = (
	'PROGRAM',
	'VAR',
	'INT',
	'FLOAT',
	'PRINT',
	'IF',
	'ELSE',
	'IDENTIFICADOR',
	'CONST_INT',
	'CONST_FLOAT',
	'CONST_STRING',
	'DOS_PUNTOS',
	'COMA',
	'PUNTOCOMA',
	'LLI',
	'LLD',
	'PARENI',
	'PAREND',
	'MENOR',
	'MAYOR',
	'DIFERENTE',
	'MAS',
	'MENOS',
	'POR',
	'ENTRE',
	'IGUAL'
)

#Tokens
t_MAS 			= r'\+'
t_MENOS 		= r'-'
t_POR 			= r'\*'
t_ENTRE			= r'/'
t_IGUAL			= r'='
t_PARENI		= r'\('
t_PAREND		= r'\)'
t_MENOR			= r'\<'
t_MAYOR			= r'\>'
t_DIFERENTE		= r'\<\>'
t_DOS_PUNTOS	= r'\:'
t_COMA			= r'\,'
t_PUNTOCOMA		= r';'
t_LLI			= r'\{'
t_LLD			= r'\}'
t_CONST_STRING  = r'\"[A-Za-z0-9]+\"'

def t_IDENTIFICADOR(t):
	r'[a-z][a-zA-Z0-9]*'
	t.type = reserved.get(t.value, 'IDENTIFICADOR')
	return t

def t_CONST_INT(t):
	r'\[0-9]+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Valor entero demasiado grande %d", t.value)
		t.value = 0
	return t

def t_CONST_FLOAT(t):
	r'[0-9]+\.[0-9]+([Ee](\+|\-)?[0-9]+)'
	try:
		t.value = float(t.value)
	except ValueError:
		print("Valor flotante demasiado grande %f", t.value)
		t.value = 0.00
	return t
	
#Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	print("Caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

#Construccion del lexer
import ply.lex as lex
lex.lex()

#Reglas de parsing
precendence =(
	('left', 'MAS', 'MENOS'),
	('left', 'POR', 'ENTRE'),
	)	

#Directorio de nombres
names = { }

def p_start(t):
    'start : PROGRAM IDENTIFICADOR PUNTOCOMA prog bloque'
	
def p_prog(t):
	'''prog : vars
			| '''

def p_vars(t):
	'vars : VAR vars1'
	
def p_vars1(t):
	'''vars1 : vars2 DOS_PUNTOS tipo PUNTOCOMA vars1
			| '''
			
def p_vars2(t):
	'vars2 : IDENTIFICADOR vars3'
	
def p_vars3(t):
	'''vars3 : COMA vars2 
			| '''

def p_bloque(t):
	'bloque : LLI bloque1 LLD'
	
def p_bloque1(t):
	'''bloque1 : estatuto bloque1
			| '''

def p_tipo(t):
	'''tipo : INT
		| FLOAT '''

def p_estatuto(t):
	'''estatuto : asignacion
		| condicion
		| escritura'''

def p_asignacion(t):
	'asignacion : IDENTIFICADOR IGUAL expresion PUNTOCOMA'
	
def p_expresion(t):
	'expresion : exp expresion1'

def p_expresion1(t):
	'''expresion1 : MAYOR exp
		| MENOR exp
		| DIFERENTE exp
		| '''
		
def p_exp(t):
	'exp : termino exp1'

def p_exp1(t):
	'''exp1 : MAS exp1
		| MENOS exp1
		| '''
		
def p_termino(t):
	'termino : factor termino1'

def p_termino1(t):
	'''termino1 : POR termino1
		| ENTRE termino1
		| '''

def p_factor(t):
	'factor : factor1'

def p_factor1(t):
	'''factor1 : PARENI expresion PAREND
		| varcte'''

#FAlta poner el signo

def p_varcte(t):
	'''varcte : IDENTIFICADOR
		| CONST_INT
		| CONST_FLOAT '''

def p_condicion(t):
	'condicion : IF PARENI expresion PAREND bloque cond PUNTOCOMA'

def p_cond(t):
	'''cond : ELSE bloque
		| '''

def p_escritura(t):
	'escritura : PRINT PARENI escritura1 PAREND PUNTOCOMA'

def p_escritura1(t):
	'''escritura1 : escr
		| CONST_STRING '''

def p_escr(t):
	'escr : expresion escr1'

def p_escr1(t):
	'''escr1 : expresion escr1
		| '''

def p_error(t):
	print("Error de sintaxis en '%s'" % t.value)
	
import ply.yacc as yacc
yacc.yacc()

s = open('testcase', 'r').read()
yacc.parse(s)
