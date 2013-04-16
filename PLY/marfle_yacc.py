#Marfle - Sintaxis
#Compiladores - TC3040
#
#Rubén Alejandro Valdez Ruiz 803015
#Ana Guajardo
#

import sys, collections, math

#Hace la importación de los tokes del lenguaje
from marfle_lex import tokens

#Importa el módulo de YACC para el parseo
import ply.yacc as yacc

#Hace la importación delcubo semático
from cuboSem import cuboSem


## ARCHIVO DONDE SE ESCRIBIRÁN LOS CUÁDRUPLOS
cuadruplos = open('cuadruplos', 'w')

temporal = 1

#Verifica la versión de Python para la entrada de datos
if sys.version_info[0] < 3:
    input = raw_input

# STACKS DEL LENGUAJE

pilaO   =   []
pOper   =   []
pSaltos =   []
pTipos  =   []


################################################################################
'''
    Creación de la estructura de Tabla de Variables
'''
#var = collections.namedtuple('Var', 'name type dim')
var = collections.namedtuple('Var', 'type dim')
#test = {'a': var2('int', [])}
#test['b'] = var2('float', [3,4])

#print(test)
#print(test['b'])

varname = ''
vartype = ''
vardim1 = ''
vardim2 = ''
################################################################################

################################################################################
'''
    Creación de la estructura de Directorio de Procedimientos
'''
DirProc = collections.namedtuple('DirProc', 'tipoRet params vars')
#DirProc2 = collections.namedtuple('DirProc2', 'tipoRet vars')
dirProc = {}
modRet = ''
modActual = ''
modParamType = ''
################################################################################


################################################################################
'''
    Creación de la estructura para los objetos
'''
Objeto = collections.namedtuple('Objeto', 'herencia vars mods')
objetos = {}

#Variable de objeto, tiene visibilidad, tipo y dimensión
VarObj = collections.namedtuple('VarObj', 'vis type dim')
varobjs = {}
objActual = ''
visibilidad = ''
################################################################################


################################################################################
'''
    Creación de la lista de cuádruplos
'''
Cuadruplo = collections.namedtuple('Cuadruplo', ' pos op oper1 oper2 res')
cuad = []
cont = 0
################################################################################




#Especificación de precedencia de operadores
precedence = (
    ('nonassoc', 'MENQUE','MAYQUE','MAYIGU','MENIGU','DIFERE'),
    ('left',    'AND', 'OR'),
    ('left',    'MAS', 'MENOS'),
    ('left',    'POR', 'DIVISI'),
    ('right',   'UMENOS', 'IGUAL') #UMENOS es el negativo UNARIO
)

#REGLAS DEL LENGUAJE
################################################################################

# PROGRAM
def p_program(p):
    'program : PROGRAM IDENTI semCreaDP cuadInicial LBRACK progobj progvars progmod main RBRACK'
    print("\n***Entrada aceptada***\n")

def p_progobj(p):
    '''progobj  : objeto progobj
                |'''

def p_progvars(p):
    '''progvars : vars'''

def p_progmod(p):
    '''progmod  : modulo progmod
                |'''

#####SEMÁNTICA DE PROGRAM
def p_semCreaDP(p):
    'semCreaDP  :'
    global dirProc, modActual
    #dirProc.append(DirProc(p[-1], 'global', []))
    dirProc['main'] = DirProc('global', {}, {})
    modActual = 'main'
    #print(dir2)

def p_cuadInicial(p):
    'cuadInicial    :'
    global cont
    cuad.append(Cuadruplo(cont, 19, -1, -1, -1))
    cont += 1

#MAIN
def p_main(p):
    'main   : MAIN LPAREN RPAREN iniciaMain bloque'
    
def p_iniciaMain(p):
    'iniciaMain :'
    global modActual
    cuad[0] = Cuadruplo(0, 19, -1, -1, cont)
    modActual = 'main'

#OBJETO
def p_objeto(p):
    'objeto : OBJECT IDENTI foundObjID herencia LBRACK objvars vieneAsignacion objmet RBRACK acabaOBJ'

def p_herencia(p):
    '''herencia : LPAREN IDENTI RPAREN
                |'''

def p_objmet(p):
    '''objmet   : modulo objmet
                |'''

def p_foundObjID(p):
    'foundObjID :'
    global objActual
    objActual = p[-1]
    objetos[p[-1]] = Objeto({},{},{})
    
def p_vieneAsignacion(p):
    '''vieneAsignacion  :   asignacion masAsign
                        |   '''
    
def p_masAsign(p):
    '''masAsign     :   asignacion masAsign
                    |   '''

def p_acabaOBJ(p):
    'acabaOBJ   :'
    global modActual, objActual
    modActual = 'main'
    objActual = None

#BLOQUE
def p_bloque(p):
    'bloque :   LBRACK bloq RBRACK'

def p_bloq(p):
    '''bloq :   estret
            |'''

def p_estret(p):
    '''estret   :   estatuto bloq
                |   return bloq
                |   varcte bloq'''

#ESTATUTO
def p_estatuto(p):
    '''estatuto :   lectura
                |   asignacion
                |   condicion
                |   escritura
                |   ciclo'''
    #Ver sobre la regla de METCALL

#VARS
def p_vars(p):
    '''vars     :   tipo IDENTI vartam SEMCOL insertVar varsagain'''
    

def p_vartam(p):
    '''vartam   :   tamano
                |'''

def p_varsagain(p):
    '''varsagain    :   vars
                    |   ENDVAR SEMCOL'''

def p_objvars(p):
    'objvars    :   visibilidad tipo IDENTI vartam insertObjVar SEMCOL delVis objvarsagain'

def p_visibilidad(p):
    '''visibilidad  :   PUBLIC foundKeyword
                    |   PRIVATE foundKeyword'''

def p_foundKeyword(p):
    'foundKeyword   :'
    global visibilidad
    visibilidad = p[-1]

def p_insertObjVar(p):
    'insertObjVar   :'
    global visibilidad, vartype, vardim1, objActual
    objetos[objActual].vars[p[-2]] = VarObj(visibilidad, vartype, vardim1)
    #print(objetos)

def p_delVis(p):
    'delVis :'
    global visibilidad
    visibilidad = ''

def p_objvarsagain(p):
    '''objvarsagain :   objvars
                    |   ENDVAR SEMCOL
                    |'''

def p_insertVar(p):
    'insertVar  :   '
    global vartype, vardim1, modActual, objActual
    
    if objActual is not None:
        #print(modActual)
        #print(objActual)
        if p[-3] not in objetos[objActual].mods[modActual].vars:
            objetos[objActual].mods[modActual].vars[p[-3]] = var(vartype, vardim1)
        else:
            sys.exit("Variable ya declarada\n")
    else:
    
        if p[-3] not in dirProc[modActual].vars:
            dirProc[modActual].vars[p[-3]] = var(vartype, vardim1)
        else:
            sys.exit("Variable ya declarada\n")
    #print(dirProc[modActual])
    vardim1 = []
                    
#TAMAÑO
def p_tamano(p):
    'tamano :   LCORCH CONINT metearr RCORCH tammatriz'
    global vardim1
    #vardim1 = [p[2]]
    #print(vardim1)

def p_metearr(p):
    'metearr    :'
    global vardim1
    vardim1 = [p[-1]]

#TAMMATRIZ
def p_tammatriz(p):
    '''tammatriz    :   LCORCH CONINT RCORCH
                    |'''
    global vardim2
    if len(p) > 1:
        vardim1.append(p[2])
        #print(vardim2)

#RETURN
def p_return(p):
    'return :   RETURN superexpresion SEMCOL'
    global cont
    oper1 = pilaO.pop()
    #cuadruplos.write("(16,\t,\t,\t%s)\n" % (oper1))
    cuad.append(Cuadruplo(cont, '15', -1, -1, oper1))
    cont += 1

#ASIGNACION
def p_asignacion(p):
    'asignacion :   IDENTI foundID dimension IGUAL foundEQ exp SEMCOL'
    operador = pOper.pop()
    oper1 = pilaO.pop()
    tipo1 = pTipos.pop()
    operIgualado = pilaO.pop()
    tipo2 = pTipos.pop()
    tipoRes = cuboSem[tipo2][tipo1][operador]
    if tipoRes is not -1:
        global cont
        cuad.append(Cuadruplo(cont, operador, oper1, -1, operIgualado))
        cont += 1
    #print(pilaO)
    
def p_foundID(p):
    'foundID    :'
    global modActual, objActual
    #El primer IF es el que revisa la parte de las variables de objeto
    if objActual is not None:
        
        if p[-1] in objetos[objActual].vars:
            pTipos.append(objetos[objActual].vars[p[-1]].type)
            pilaO.append(p[-1])
        elif p[-1] in objetos[objActual].mods[modActual].vars:
            pTipos.append(objetos[objActual].mods[modActual].vars[p[-1]].type)
            pilaO.append(p[-1])    
        
    elif p[-1] in dirProc[modActual].vars:
        pTipos.append(dirProc[modActual].vars[p[-1]].type)
        pilaO.append(p[-1])
    elif p[-1] in dirProc:
        #Creación del ERA y demás cosas de llamada a módulos.
        print("Yay!")
    else:
        #print(dirProc[modActual])
        print(dirProc)
        sys.exit("Variable NO declarada!! %s" % (p.lexer.lineno))

def p_foundEQ(p):
    'foundEQ    :'
    pOper.append(10)

#ESCRITURA
def p_escritura(p):
    'escritura  :   PRINT LPAREN prntparam RPAREN SEMCOL'
    
    oper1 = pilaO.pop()
    tipo1 = pTipos.pop()
    global cont
    cuad.append(Cuadruplo(cont, '14', -1, -1, oper1))
    cont += 1

def p_prntparam(p):
    '''prntparam    :   superexpresion
                    |'''

#LECTURA
def p_lectura(p):
    'lectura    :   READ LPAREN IDENTI dimobj RPAREN SEMCOL'

def p_dimobj(p):
    '''dimobj   :   dimension
                |   PUNTO IDENTI'''

#CONDICION - IF
def p_condicion(p):
    'condicion  :   IF LPAREN superexpresion RPAREN genCuadIF bloque tieneelse'

def p_tieneelse(p):
    '''tieneelse    :   ELSE genCuadElse bloque acabaIF
                    |   acabaIF'''

def p_genCuadIF(p):
    'genCuadIF  :'
    global cont
    res = pilaO.pop()
    tipo = pTipos.pop()
    cuad.append(Cuadruplo(cont, '16', res, -1, -1))
    pSaltos.append(cont)
    cont += 1

def p_acabaIF(p):
    'acabaIF    :'
    fin = pSaltos.pop()
    #print("\n")
    #print(cuad[fin])
    pos = cuad[fin].pos
    op = cuad[fin].op
    oper1 = cuad[fin].oper1
    oper2 = cuad[fin].oper2
    
    cuad[fin]= Cuadruplo(pos, op, oper1, oper2, cont)

def p_genCuadElse(p):
    'genCuadElse    :'
    global cont
    cuad.append(Cuadruplo(cont, 18, -1, -1, -1))
    cont += 1
    falso = pSaltos.pop()
    pos = cuad[falso].pos
    op = cuad[falso].op
    oper1 = cuad[falso].oper1
    oper2 = cuad[falso].oper2
    cuad[falso] = Cuadruplo(pos, op, oper1, oper2, cont)
    pSaltos.append(cont-1)
    

#CICLO
def p_ciclo(p):
    '''ciclo    :   dowhile
                |   for
                |   while'''

#DOWHILE
def p_dowhile(p):
    'dowhile    :   DO doMeteCont bloque WHILE LPAREN superexpresion RPAREN SEMCOL doTermina'

def p_doMeteCont(p):
    'doMeteCont :'
    global cont
    pSaltos.append(cont)

def p_doTermina(p):
    'doTermina  :'
    global cont
    retorno = pSaltos.pop()
    resultado = pilaO.pop()
    tipo = pTipos.pop()
    cuad.append(Cuadruplo(cont, 17, resultado,  -1, retorno))
    cont += 1

#WHILE
def p_while(p):
    'while  :   WHILE meteContWhile LPAREN superexpresion RPAREN whileGeneraFalso bloque whileTermina'

def p_meteContWhile(p):
    'meteContWhile  :'
    global cont
    pSaltos.append(cont)

def p_whileGeneraFalso(p):
    'whileGeneraFalso   :'
    global cont
    resultado = pilaO.pop()
    tipo = pTipos.pop()
    cuad.append(Cuadruplo(cont, 16, resultado,  -1, -1))
    pSaltos.append(cont)
    cont += 1

def p_whileTermina(p):
    'whileTermina   :'
    global cont
    falso = pSaltos.pop()
    retorno = pSaltos.pop()
    cuad.append(Cuadruplo(cont, 18, -1, -1, retorno))
    cont += 1
    
    pos = cuad[falso].pos
    op = cuad[falso].op
    oper1 = cuad[falso].oper1
    oper2 = cuad[falso].oper2
    cuad[falso] = Cuadruplo(pos, op, oper1, oper2, cont)

#FOR
def p_for(p):
    'for    :   FOR LPAREN IDENTI dimension IGUAL exp SEMCOL superexpresion SEMCOL IDENTI dimension IGUAL exp RPAREN bloque'

#DIMENSION
def p_dimension(p):
    '''dimension    :   LCORCH exp RCORCH matriz
                    |'''

#MATRIZ
def p_matriz(p):
    '''matriz   :   LCORCH exp RCORCH
                |'''

#TERMINO
def p_termino(p):
    'termino    :   factor term'

def p_term(p):
    '''term :   POR foundMUDI factor genCuadMUDI term
            |   DIVISI foundMUDI factor genCuadMUDI term
            |'''

def p_foundMUDI(p):
    'foundMUDI  :'
    if(p[-1] == '*'):
        pOper.append(2)
    elif(p[-1] == '/'):
        pOper.append(3)

def p_genCuadMUDI(p):
    'genCuadMUDI    :'
    operador = pOper.pop()
    oper2 = pilaO.pop()
    oper1 = pilaO.pop()
    
    tipo2 = pTipos.pop()
    tipo1 = pTipos.pop()
    #print(pTipos)
    global temporal, cont
    tipoRes = cuboSem[tipo1][tipo2][operador]
    if(tipoRes != -1):
        pTipos.append(tipoRes)
        pilaO.append("t_%s" % temporal)
        #cuadruplos.write("(%s,\t%s,\t%s,\tt_%s)\n" % (operador,oper1,oper2,temporal))
        cuad.append(Cuadruplo(cont, operador, oper1, oper2, "t_%s" % temporal))
    cont += 1
    temporal += 1

#FACTOR
def p_factor(p):
    '''factor   :   LPAREN foundLP exp RPAREN foundRP
                |   menunario varcte'''
    

def p_menunario(p):
    '''menunario    :   MENOS %prec UMENOS
                    |'''

def p_foundLP(p):
    'foundLP    :'
    pOper.append(p[-1])
    #print(pOper)
    
def p_foundRP(p):
    'foundRP    :'
    #print(pOper[len(pOper)-1])
    if(pOper[len(pOper)-1] == '('):
        pOper.pop()
    else:
        sys.exit("Número impar de paréntesis!!")

#MODULO
def p_modulo(p):
    'modulo :   FUNC modtipo IDENTI semCreaMod LPAREN modparams RPAREN modbloque'
    

def p_modtipo(p):
    '''modtipo  :   tipos
                |   VOID'''
    global modRet
    if(p[1] == 'void'):
        modRet = 'void'

def p_modparams(p):
    '''modparams    :   tipos IDENTI foundParam masmodparams
                    |'''
def p_foundParam(p):
    'foundParam :'
    global modParamType, modActual, objActual
    print(p[-1])
    if objActual is not None and modActual is not None:
        print(objetos)
        objetos[objActual].mods[modActual].params[p[-1]] = modParamType
    
    if modActual is not None:
        print(dirProc)

def p_masmodparams(p):
    '''masmodparams :   SEMCOL modparams
                    |'''

def p_modbloque(p):
    'modbloque  :   LBRACK vars modbloq RBRACK'

#def p_modvars(p):
#    '''modvars  :   tipos IDENTI vartam SEMCOL modvars
#                |'''


def p_modbloq(p):
    '''modbloq  :   estatuto modbloq
                |   return modbloq
                |   varcte modbloq
                |'''

#####SEMÁNTICA DE MODULO
def p_semCreaMod(p):
    'semCreaMod :'
    #dirProc.append(DirProc(p[-1], modRet, []))
    global modActual, objActual
    if objActual is not None:
        objetos[objActual].mods[p[-1]] = DirProc(modRet, {}, {})
        modActual = p[-1]
        #print(objetos)
    else:
        modActual = p[-1]
    #print(modActual)
        dirProc[p[-1]] = DirProc(modRet, {}, {})
    #print(dirProc)

#VARCTE
def p_varcte(p):
    '''varcte   :   otrasconst
                |   cteid'''

def p_cteid(p):
    'cteid  :   IDENTI foundID funcdimobj'
    
def p_funcdimobj(p):
    '''funcdimobj   :   LPAREN exp mascall RPAREN SEMCOL
                    |   dimension
                    |   PUNTO IDENTI dimobjcall'''

def p_mascall(p):
    '''mascall  :   COMMA exp mascall
                |'''

def p_dimobjcall(p):
    '''dimobjcall   :   dimension
                    |   LPAREN exp mascall RPAREN'''

def p_otrasconst(p):
    '''otrasconst   :   CONFLO foundNUMFLO
                    |   CONINT foundNUMINT
                    |   conbol
                    |   CONSTR foundSTR'''


def p_foundNUMINT(p):
    'foundNUMINT   :'
    pTipos.append(0)
    pilaO.append(p[-1])
    #print(pTipos)

def p_foundNUMFLO(p):
    'foundNUMFLO    :'
    pTipos.append(1)
    pilaO.append(p[-1])
    #print(pTipos)

def p_foundSTR(p):
    'foundSTR   :'
    pTipos.append(3)
    pilaO.append(p[-1])

def p_conbol(p):
    '''conbol   :   TRUE foundBOOL
                |   FALSE foundBOOL'''

def p_foundBOOL(p):
    'foundBOOL  :'
    pTipos.append(2)
    pilaO.append(p[-1])

#TIPO
def p_tipo(p):
    '''tipo :   tipos
            |   IDENTI isobject'''

def p_isobject(p):
    'isobject   :   '
    global vartype
    vartype = p[-1]

#TIPOS
def p_tipos(p):
    '''tipos    :   INT
                |   FLOAT
                |   STRING
                |   BOOL'''
    global modRet, vartype, objActual, modActual, modParamType
    if(p[-1] == 'func'):
        modRet = p[1]
        #print(modRet)
    if(p[1] == 'int'):
        vartype = 0
    elif(p[1] == 'float'):
        vartype = 1
    elif(p[1] == 'bool'):
        vartype = 2
    elif(p[1] == 'string'):
        vartype = 3
    
    if modActual is not None:
        modParamType = p[-1]
    
#EXPRESION
def p_expresion(p):
    '''expresion    :   NOT exp
                    |   exp compara'''

def p_compara(p):
    '''compara  :   MENQUE foundComp exp genCuadMUDI
                |   MAYQUE foundComp exp genCuadMUDI
                |   DIFERE foundComp exp genCuadMUDI
                |   MENIGU foundComp exp genCuadMUDI
                |   MAYIGU foundComp exp genCuadMUDI
                |   IGUIGU foundComp exp genCuadMUDI
                |'''
                
def p_foundComp(p):
    'foundComp  :'
    if(p[-1] == '<'):
        pOper.append(4)
    elif(p[-1] == '>'):
        pOper.append(5)
    elif(p[-1] == '<='):
        pOper.append(7)
    elif(p[-1] == '>='):
        pOper.append(8)
    elif(p[-1] == '=='):
        pOper.append(9)
    elif(p[-1] == '!='):
        pOper.append(6)
                
#EXP
def p_exp(p):
    'exp    :   termino expre'
    
def p_expre(p):
    '''expre    :   MAS foundPLMI termino genCuadMUDI expre
                |   MENOS foundPLMI termino genCuadMUDI expre
                |'''

def p_foundPLMI(p):
    'foundPLMI  :'
    if(p[-1] == '+'):
        pOper.append(0)
    elif(p[-1] == '-'):
        pOper.append(1)
    #pOper.append(p[-1])

#SUPEREXPRESION
def p_superexpresion(p):
    'superexpresion :   expresion superexp'

def p_superexp(p):
    '''superexp :   logicos
                |'''

def p_logicos(p):
    'logicos    :   andor expresion genCuadMUDI maslogicos'

def p_andor(p):
    '''andor    :   AND foundANDOR
                |   OR foundANDOR'''

def p_foundANDOR(p):
    'foundANDOR :'
    if(p[-1] == '&&'):
        pOper.append(11)
    elif(p[-1] == '||'):
        pOper.append(12)
    #print(pOper)

def p_maslogicos(p):
    '''maslogicos   :   logicos
                    |'''
                    
#ERRORES DE PARSING
def p_error(p):
    sys.exit("Error de Sintaxis en '%s', renglón '%s'" % (p.value, p.lexer.lineno))


#ENTRADA DE DATOS AL PARSER
#Se toma la entrada del archivo "testcase"
yacc.yacc()
s = open('testcase', 'r').read()
yacc.parse(s)
#print("\n%s\n" % dirProc)

#print(pOper)
#print(pilaO)

for cu in cuad:
    print("%s\t| %s,\t%s,\t%s,\t%s" % (cu.pos, cu.op, cu.oper1, cu.oper2, cu.res))
    cuadruplos.write("%s,\t%s,\t%s,\t%s,\t%s\n" % (cu.pos, cu.op, cu.oper1, cu.oper2, cu.res))

cuadruplos.close()

'''
for dirs in dirProc.keys():
    print("Módulo\n***************\nNombre\tTipo")
    print("%s\t%s" % (dirs, dirProc[dirs].tipoRet))
    print("\nVariables de módulo")
    print("Nombre\tTipo\tDimensión")
    for varis in dirProc[dirs].vars.keys():
        print("%s\t%s\t%s" % (varis, dirProc[dirs].vars[varis].type, dirProc[dirs].vars[varis].dim))
    print("***************\n")
    
print("****OBJETOS****")
for objeto in objetos:
    print("%s\n%s" % (objetos[objeto].vars,objetos[objeto].mods))
'''

#print(objetos)