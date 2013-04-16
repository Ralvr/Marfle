#Marfle - Léxico
#Compiladores - TC3040
#
#Rubén Alejandro Valdez Ruiz 803015
#Ana Guajardo
#
#

import sys
import ply.lex as lex
#lex.lex()

if ".." not in sys.path: sys.path.insert(0, "..")

#Revisa la versión de Python instalada
if sys.version_info[0] < 3:
    input = raw_input
    

#Palabras reservadas del lenguaje
reserved = {
    'program'   :   'PROGRAM',
    'while'     :   'WHILE',
    'string'    :   'STRING',
    'read'      :   'READ',
    'if'        :   'IF',
    'do'        :   'DO',
    'main'      :   'MAIN',
    'else'      :   'ELSE',
    'int'       :   'INT',
    'print'     :   'PRINT',
    'bool'      :   'BOOL',
    'for'       :   'FOR',
    'float'     :   'FLOAT',
    'object'    :   'OBJECT',
    'endvar'    :   'ENDVAR',
    'void'      :   'VOID',
    'func'      :   'FUNC',
    'return'    :   'RETURN',
    'public'    :   'PUBLIC',
    'private'   :   'PRIVATE',
    'true'      :   'TRUE',
    'false'     :   'FALSE'
}

#tokens
tokens = [
    'LPAREN',
    'RPAREN',
    'LCORCH',
    'RCORCH',
    'LBRACK',
    'RBRACK',
    'MAS',
    'MENOS',
    'POR',
    'DIVISI',
    'IGUAL',
    'MENQUE',
    'MAYQUE',
    'MENIGU',
    'MAYIGU',
    'DIFERE',
    'IGUIGU',
    'AND',
    'OR',
    'NOT',
    'COMMA',
    'PUNTO',
#    'DOSPUN',
    'SEMCOL',
    'IDENTI',
    'CONINT',
    'CONFLO',
    'CONSTR'
] + list(reserved.values())

#literals = ['.']

#Definicion de tokens
t_LPAREN    =   r'\('
t_RPAREN    =   r'\)'
t_LCORCH    =   r'\['
t_RCORCH    =   r'\]'
t_LBRACK    =   r'\{'
t_RBRACK    =   r'\}'
t_MAS       =   r'\+'
t_MENOS     =   r'\-'
t_POR       =   r'\*'
t_DIVISI    =   r'\/'
t_IGUAL     =   r'\='
t_MENQUE    =   r'\<'
t_MAYQUE    =   r'\>'
t_MENIGU    =   r'\<\='
t_MAYIGU    =   r'\>\='
t_DIFERE    =   r'\!\='
t_IGUIGU    =   r'\=\='
t_AND       =   r'\&\&'
t_OR        =   r'\|\|'
t_NOT       =   r'\!'
t_PUNTO     =   r'\.'
t_COMMA     =   r'\,'
#t_DOSPUN    =   r'\:'
t_SEMCOL    =   r'\;'
#t_COMILL    =   r'\"'
t_CONSTR    =   r'\"[A-Za-z0-9]+\"'

def t_IDENTI(t):
    r'[a-z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTI')
    return t

def t_CONFLO(t):
	r'[0-9]+\.[0-9]+'
    #r'[0-9]+\.[0-9]+([Ee](\+|\-)?[0-9]+)*'
	try:
		t.value = float(t.value)
	except ValueError:
		print("Valor flotante demasiado grande %f", t.value)
		t.value = 0.00
	return t

def t_CONINT(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero demasiado grande.")
        t.value = 0
    return t

#Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()