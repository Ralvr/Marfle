import sys
sys.path.insert(0,"../..")

if sys.version_info[0] < 3:
    input = raw_input

tokens = ('ID',)

# Token Definition
def t_ID(t):
	r'[a-z]+'
	return t

#t_MAS = r'\+'


# Ignored characters
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
	
# Build Lexer
import ply.lex as lex
lex.lex()

# Parsing rules

def p_start(p):
	'start : ID ID ID'
	print("Se aceptó un:", p[1], p[2], p[3])

def p_error(p):
	print("Syntax error at '%s'" % p.value)
	
import ply.yacc as yacc
yacc.yacc()

s = open('testcase', 'r').read()
yacc.parse(s)