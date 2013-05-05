#coding=UTF-8
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

mem = collections.namedtuple('Memoria', 'int float bool str')
#MemGlobal       =   mem({},{},{},{})
MemConstante    =   mem({},{},{},{})
MemTemporal     =   mem({},{},{},{})
MemGlobal       =   mem({},{},{},{})
MemLocal        =   mem({},{},{},{})
MemObjeto       =   mem({},{},{},{})
stackLocalMaster = []

######  MEMORIA GLOBAL
##############                  INT
MemGlobalINTCont = 2500
MemGlobalINTOffset = 0

##############                  FLOAT
MemGlobalFLOCont = 5000
MemGlobalFLOOffset = 0

##############                  BOOL
MemGlobalBOLCont = 7500
MemGlobalBOLOffset = 0

##############                  STRING
MemGlobalSTRCont = 10000
MemGlobalSTROffset = 0

######  MEMORIA TEMPORAL
##############                  INT
MemTempINTCont = 22500
MemTempINTOffset = 0

##############                  FLOAT
MemTempFLOCont = 25000
MemTempFLOOffset = 0

##############                  BOOL
MemTempBOLCont = 27500
MemTempBOLOffset = 0

##############                  STRING
MemTempSTRCont  = 30000
MemTempSTROffset    = 0


######  MEMORIA LOCAL
MemLocalINTCont = 12500
MemLocalINTOffset = 0

MemLocalFLOCont = 15000
MemLocalFLOOffset = 0

MemLocalBOLCont = 17500
MemLocalBOLOffset = 0

MemLocalSTRCont = 20000
MemLocalSTROffset = 0


######MEMORIA CONSTANTE
##############                  INT
#Contador de Memoria constante
MemConstanteINTCont = 32500
MemConstanteINTOffset = 0

##############                  FLOAT
#Contador de Memoria flotante
MemConstanteFLOCont = 35000
MemConstanteFLOOffset = 0

##############                  BOOL
#Contador de Memoria Booleana
MemConstanteBOLCont = 37500
MemConstanteBOLOffset = 0

##############                  STRING
MemConstanteSTRCont = 40000
MemConstanteSTROffset = 0

#######MEMORIA DE OBJETOS

tipoObjeto = {}



varObjeto = {}
#varObjetoOffset = 0

MemObjetoINT = 50000
MemObjetoINTOffset = 0

MemObjetoFLO = 52500
MemObjetoFLOOffset = 0

MemObjetoBOL = 55000
MemObjetoBOLOffset = 0

MemObjetoSTR = 57500
MemObjetoSTROffset = 0



################################################################################
'''
    Creación de la estructura de Tabla de Variables
'''
var = collections.namedtuple('Var', 'type dim dirV')

varname = ''
vartype = ''
vardim1 = ''
vardim2 = ''
m0 = 0
retOp = ''
retTyp = ''
################################################################################

Dim = collections.namedtuple('Dim', 'lsup linf mn')
dim = {}
#dim['dim1'] = Dim(3,0,0)
#print(dim)


################################################################################
'''
    Creación de la estructura de Directorio de Procedimientos
'''
DirProc = collections.namedtuple('DirProc', 'tipoRet params vars inicio')
dirProc = {}
modRet = ''
modActual = ''
modSiguiente = ''
modParamType = ''
modParams = 1
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
    global dirProc, modActual, cont
    #dirProc.append(DirProc(p[-1], 'global', []))
    dirProc['main'] = DirProc('global', {}, {}, cont)
    modActual = 'main'
    #print(dir2)

def p_cuadInicial(p):
    'cuadInicial    :'
    global cont
    cuad.append(Cuadruplo(cont, 18, -1, -1, -1))
    cont += 1

#MAIN
def p_main(p):
    'main   : MAIN LPAREN RPAREN iniciaMain bloque'
    
def p_iniciaMain(p):
    'iniciaMain :'
    global modActual
    cuad[0] = Cuadruplo(0, 18, -1, -1, cont)
    modActual = 'main'

#OBJETO
def p_objeto(p):
    'objeto : OBJECT IDENTI foundObjID herencia LBRACK objvars vieneAsignacion objmet RBRACK acabaOBJ'

def p_herencia(p):
    '''herencia : LPAREN IDENTI RPAREN
                |'''
    if len(p) > 1:
        if p[2] in objetos:
            objetos[p[-2]] = Objeto(p[2],{}, objetos[p[2]].mods)
            for key, variable in objetos[p[2]].vars.iteritems():
                if objetos[p[2]].vars[key].vis == 'public':
                    objetos[p[-2]].vars[key] = objetos[p[2]].vars[key]
        else:
            sys.exit("Objeto %s no está delcarado." % p[2])


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
    #print(objetos[objActual])
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
    global visibilidad, vartype, vardim1, objActual, dim
    objetos[objActual].vars[p[-2]] = VarObj(visibilidad, vartype, dim)
    dim = {}
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
            objetos[objActual].mods[modActual].vars[p[-3]] = var(vartype, dim, 0)
        else:
            sys.exit("Variable ya declarada\n")
    else:
        if p[-3] not in dirProc[modActual].vars:
            global MemGlobalINTCont, MemGlobalINTOffset, MemGlobalFLOCont, MemGlobalFLOOffset, MemGlobalBOLCont, MemGlobalBOLOffset, MemGlobalSTRCont, MemGlobalSTROffset, MemLocalINTCont, MemLocalINTOffset, varObjeto, vardim1, vardim2, dim, m0
            #print(vartype)
            if modActual == 'main':
                if vartype == 0:
                    dirProc[modActual].vars[p[-3]] = var(vartype, dim, MemGlobalINTCont + MemGlobalINTOffset)
                    if m0 is not 0:
                        MemGlobalINTOffset +=  m0
                    else:
                        MemGlobalINTOffset +=  1
                elif vartype == 1:
                    dirProc[modActual].vars[p[-3]] = var(vartype, dim, MemGlobalFLOCont + MemGlobalFLOOffset)
                    if m0 is not 0:
                        MemGlobalFLOOffset += m0
                    else:
                        MemGlobalFLOOffset += 1
                elif vartype == 2:
                    dirProc[modActual].vars[p[-3]] = var(vartype, dim, MemGlobalBOLCont + MemGlobalBOLOffset)
                    if m0 is not 0:
                        MemGlobalBOLOffset += m0
                    else:
                        MemGlobalBOLOffset += 1
                elif vartype == 3:
                    dirProc[modActual].vars[p[-3]] = var(vartype, dim, MemGlobalSTRCont + MemGlobalSTROffset)
                    if m0 is not 0:
                        MemGlobalSTROffset += m0
                    else:
                        MemGlobalSTROffset += 1
                elif vartype in objetos:
                    dirProc[modActual].vars[p[-3]] = var(vartype, dim, 0)
                    varObjeto[p[-3]] = mem({},{},{},{})
                    #tipoObjeto[vartype] = varObjeto + varObjetoOffset
                m0 = 0

            else:
                if vartype == 0:
                    dirProc[modActual].vars[p[-3]] =var(vartype, dim, MemLocalINTCont + MemLocalINTOffset)
                    MemLocalINTOffset += 1 
                else:    
                    dirProc[modActual].vars[p[-3]] = var(vartype, dim, 0)
        else:
            sys.exit("Variable ya declarada\n")
    #print(dirProc[modActual])
    vardim1 = {}
    vardim2 = {}
    dim = {}

                    
#TAMAÑO
def p_tamano(p):
    'tamano :   LCORCH CONINT metearr RCORCH tammatriz'
    global vardim1
    #vardim1 = [p[2]]
    #print(vardim1)

def p_metearr(p):
    'metearr    :'
    global vardim1
    vardim1 = p[-1]
    dim['dim1'] = Dim(p[-1], 0, 0)


#TAMMATRIZ
def p_tammatriz(p):
    '''tammatriz    :   LCORCH CONINT RCORCH
                    |   '''
    global vardim2, m0
    if len(p) > 1:
        dim['dim1'] = Dim(vardim1, 0, p[2])
        dim['dim2'] = Dim(p[2], 0, 0)
        m0 = vardim1 * p[2]

#RETURN
def p_return(p):
    'return :   RETURN superexpresion SEMCOL'
    global cont, retOp, retTyp, temporal, MemTempINTCont, MemTempINTOffset
    print(pilaO)
    oper1 = pilaO.pop()
    retOp = oper1
    tipo = pTipos.pop()
    retTyp = tipo
    cuad.append(Cuadruplo(cont, 15, -1, -1, MemTempINTCont + MemTempINTOffset))
    pilaO.append(MemTempINTCont + MemTempINTOffset)
    pTipos.append(retTyp)
    MemTempINTOffset += 1
    cont += 1

#ASIGNACION
def p_asignacion(p):
    'asignacion :   IDENTI tieneObjeto IGUAL foundEQ exp SEMCOL'
    print(pilaO)
    '''for cu in cuad:
                    print(cu)
                print("\n")'''
    operador = pOper.pop()
    oper1 = pilaO.pop()
    tipo1 = pTipos.pop()
    operIgualado = pilaO.pop()
    tipo2 = pTipos.pop()
    print(tipo1, tipo2, operador)
    tipoRes = cuboSem[tipo2][tipo1][operador]
    print(tipoRes)
    #print(tipo2, tipo1, operador)
    if tipoRes is not -1:
        global cont
        cuad.append(Cuadruplo(cont, operador, oper1, -1, operIgualado))
        cont += 1
    else:
        sys.exit("Tipos Inválidos en %s" % p.lexer.lineno)
    #print(pilaO)



def p_tieneObjeto(p):
    '''tieneObjeto  :   PUNTO IDENTI foundID
                    |   foundID
                    |   dimension'''
    global objActual, modActual
    #print(objActual, modActual)
    
def p_foundID(p):
    'foundID    :'
    global modActual, objActual, cont
    #print(p[-1], modActual)
    if objActual is not None:
        #Variables de objeto
        if p[-1] in objetos[objActual].vars:
            pTipos.append(objetos[objActual].vars[p[-1]].type)
            pilaO.append(p[-1])
        elif p[-1] in objetos[objActual].mods[modActual].vars:
            pTipos.append(objetos[objActual].mods[modActual].vars[p[-1]].type)
            pilaO.append(p[-1])
        elif p[-1] in objetos[objActual].mods[modActual].params:
            pTipos.append(objetos[objActual].mods[modActual].params[p[-1]])
            pilaO.append(p[-1])
        #print(pTipos)
        
    elif p[-1] in dirProc[modActual].vars:
        tipo = dirProc[modActual].vars[p[-1]].type
        if tipo == 0 or tipo == 1 or tipo == 2 or tipo == 3:
            pTipos.append(dirProc[modActual].vars[p[-1]].type)
            pilaO.append(dirProc[modActual].vars[p[-1]].dirV)
        else:
            pass
    elif p[-1] in dirProc[modActual].params:
        if 12500 <= dirProc[modActual].params[p[-1]] < 15000:
            pTipos.append(0)
            pilaO.append(dirProc[modActual].params[p[-1]])
        elif 15000 <= dirProc[modActual].params[p[-1]] < 17500:
            pTipos.append(1)
            pilaO.append(dirProc[modActual].params[p[-1]])
        elif 17500 <= dirProc[modActual].params[p[-1]] < 20000:
            pTipos.append(2)
            pilaO.append(dirProc[modActual].params[p[-1]])
        elif 20000 <= dirProc[modActual].params[p[-1]] < 22500:
            pTipos.append(3)
            pilaO.append(dirProc[modActual].params[p[-1]])
    elif p[-1] in dirProc:
        pass
    #Revisa variables de tipo objeto
    elif dirProc[modActual].vars[p[-3]].type in objetos:
        global MemObjeto, MemObjetoINT, MemObjetoINTOffset, MemObjetoFLO, MemObjetoFLOOffset, MemObjetoBOL, MemObjetoBOLOffset, MemObjetoSTR, MemObjetoSTROffset
        objActual = dirProc[modActual].vars[p[-3]].type
        tipoEs = objetos[objActual].vars[p[-1]].type
        #print(pTipos)
        #print(tipoEs)
        pTipos.append(tipoEs)
        #print(pTipos)
        if tipoEs == 0:
            #print(varObjeto)
            if p[-3] in varObjeto and p[-1] in varObjeto[p[-3]].int:
                pilaO.append(varObjeto[p[-3]].int[p[-1]])
            else:
                varObjeto[p[-3]].int[p[-1]] = MemObjetoINT + MemObjetoINTOffset
                MemObjetoINTOffset += 1
                pilaO.append(varObjeto[p[-3]].int[p[-1]])
        elif tipoEs == 1:
            if p[-3] in varObjeto and p[-1] in varObjeto[p[-3]].float:
                pilaO.append(varObjeto[p[-3]].float[p[-1]])
            else:
                varObjeto[p[-3]].float[p[-1]] = MemObjetoFLO + MemObjetoFLOOffset
                MemObjetoFLOOffset += 1
                pilaO.append(varObjeto[p[-3]].float[p[-1]])
        elif tipoEs == 2:
            if p[-3] in varObjeto and p[-1] in varObjeto[p[-3]].bool:
                pilaO.append(varObjeto[p[-3]].bool[p[-1]])
            else:
                varObjeto[p[-3]].bool[p[-1]] = MemObjetoBOL + MemObjetoBOLOffset
                MemObjetoBOLOffset += 1
                pilaO.append(varObjeto[p[-3]].bool[p[-1]])
        elif tipoEs == 3:
            if p[-3] in varObjeto and p[-1] in varObjeto[p[-3]].str:
                pilaO.append(varObjeto[p[-3]].str[p[-1]])
            else:
                varObjeto[p[-3]].str[p[-1]] = MemObjetoSTR + MemObjetoSTROffset
                MemObjetoSTROffset += 1
                pilaO.append(varObjeto[p[-3]].str[p[-1]])
        objActual = None
    #    print(pTipos)
    else:
        sys.exit("Variable NO declarada!! %s" % (p.lexer.lineno))

    #print(pTipos)

def p_foundEQ(p):
    'foundEQ    :'
    pOper.append(10)

#ESCRITURA
def p_escritura(p):
    'escritura  :   PRINT LPAREN prntparam RPAREN SEMCOL'
    
    oper1 = pilaO.pop()
    #print(oper1)
    tipo1 = pTipos.pop()
    global cont
    cuad.append(Cuadruplo(cont, 14, -1, -1, oper1))
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
    cuad.append(Cuadruplo(cont, 16, res, -1, -1))
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
    'for    :   FOR LPAREN asignacion meteContWhile superexpresion SEMCOL whileGeneraFalso asignacion RPAREN bloque whileTermina'

#DIMENSION
def p_dimension(p):
    '''dimension    :   LCORCH exp RCORCH matriz'''

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
    global temporal, cont
    #print(tipo1, tipo2)
    tipoRes = cuboSem[tipo1][tipo2][operador]
    #print(tipoRes)
    if(tipoRes != -1):
        global MemTempINTCont, MemTempINTOffset, MemTempFLOCont, MemTempFLOOffset, MemTempBOLCont, MemTempBOLOffset, MemTempSTRCont, MemTempSTROffset, modActual
        pTipos.append(tipoRes)
        if modActual == 'main':
            if tipoRes == 0:
                if MemTempINTOffset < 2500:
                    MemTemporal.int[MemTempINTCont      +   MemTempINTOffset] = "t_%s" % temporal
                    pilaO.append(MemTempINTCont      +   MemTempINTOffset)
                    cuad.append(Cuadruplo(cont, operador, oper1, oper2, MemTempINTCont + MemTempINTOffset))
                    MemTempINTOffset += 1
                else:
                    sys.exit("Demasiadas temporales enteras.")
            elif tipoRes == 1:
                if MemTempFLOOffset < 2500:
                    MemTemporal.float[MemTempFLOCont    +   MemTempFLOOffset] = "t_%s" % temporal
                    pilaO.append(MemTempFLOCont    +   MemTempFLOOffset)
                    cuad.append(Cuadruplo(cont, operador, oper1, oper2, MemTempFLOCont + MemTempFLOOffset))
                    MemTempFLOOffset += 1
                else:
                    sys.exit("Demasiadas Temporales flotantes")
            elif tipoRes == 2:
                if MemTempBOLOffset < 2500:
                    MemTemporal.bool[MemTempBOLCont     +   MemTempBOLOffset] = "t_%s" % temporal
                    pilaO.append(MemTempBOLCont     +   MemTempBOLOffset)
                    cuad.append(Cuadruplo(cont, operador, oper1, oper2, MemTempBOLCont + MemTempBOLOffset))
                    MemTempBOLOffset += 1
                else:
                    sys.exit("Demasiadas Temporales booleanas")
            elif tipoRes == 3:
                if MemTempSTROffset < 2500:
                    MemTemporal.str[MemTempSTRCont      +   MemTempSTROffset] = "t_%s" % temporal
                    pilaO.append(MemTempSTRCont      +   MemTempSTROffset)
                    cuad.append(Cuadruplo(cont, operador, oper1, oper2, MemTempSTRCont + MemTempSTROffset))
                    MemTempSTROffset += 1
                else:
                    sys.exit("Demasiadas temporales string")
        else:
            if tipoRes == 0:
                if MemTempINTOffset < 2500:
                    MemTemporal.int[MemTempINTCont      +   MemTempINTOffset] = "t_%s" % temporal
                    pilaO.append(MemTempINTCont      +   MemTempINTOffset)
                    cuad.append(Cuadruplo(cont, operador, oper1, oper2, MemTempINTCont + MemTempINTOffset))
                    MemTempINTOffset += 1
                else:
                    sys.exit("Demasiadas temporales enteras.")
            elif tipoRes == 1:
                if MemTempFLOOffset < 2500:
                    MemTemporal.float[MemTempFLOCont    +   MemTempFLOOffset] = "t_%s" % temporal
                    pilaO.append(MemTempFLOCont    +   MemTempFLOOffset)
                    cuad.append(Cuadruplo(cont, operador, oper1, oper2, MemTempFLOCont + MemTempFLOOffset))
                    MemTempFLOOffset += 1
                else:
                    sys.exit("Demasiadas Temporales flotantes")
            elif tipoRes == 2:
                if MemTempBOLOffset < 2500:
                    MemTemporal.bool[MemTempBOLCont     +   MemTempBOLOffset] = "t_%s" % temporal
                    pilaO.append(MemTempBOLCont     +   MemTempBOLOffset)
                    cuad.append(Cuadruplo(cont, operador, oper1, oper2, MemTempBOLCont + MemTempBOLOffset))
                    MemTempBOLOffset += 1
                else:
                    sys.exit("Demasiadas Temporales booleanas")
            elif tipoRes == 3:
                if MemTempSTROffset < 2500:
                    MemTemporal.str[MemTempSTRCont      +   MemTempSTROffset] = "t_%s" % temporal
                    pilaO.append(MemTempSTRCont      +   MemTempSTROffset)
                    cuad.append(Cuadruplo(cont, operador, oper1, oper2, MemTempSTRCont + MemTempSTROffset))
                    MemTempSTROffset += 1
                else:
                    sys.exit("Demasiadas temporales string")
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
    global modParamType, modActual, objActual, MemLocalINTCont, MemLocalINTOffset
    #print(p[-1])
    if objActual is not None and modActual is not None:
        objetos[objActual].mods[modActual].params[p[-1]] = modParamType
        #print(objetos)
    
    elif modActual is not None:
        #print(dirProc)
        if modParamType == 0:
            dirLActual = MemLocalINTCont + MemLocalINTOffset
            dirProc[modActual].params[p[-1]] = dirLActual
            MemLocalINTOffset += 1
        else:
            dirProc[modActual].params[p[-1]] = modParamType
        #dirProc[modActual].params[p[-1]] = modParamType
        #print(dirProc)

def p_masmodparams(p):
    '''masmodparams :   SEMCOL modparams
                    |'''

def p_modbloque(p):
    'modbloque  :   LBRACK noVars RBRACK retornoMOD'

def p_noVars(p):
    '''noVars   :   meteInicio vars modbloq
                |   meteInicio modbloq'''

def p_retornoMOD(p):
    'retornoMOD     :   '
    global cont
    cuad.append(Cuadruplo(cont, 22, -1, -1, -1))
    cont += 1

def p_meteInicio(p):
    'meteInicio     :   '
    global modActual, objActual, cont
    if objActual is not None:
        #print(objetos[objActual].mods[modActual])
        objetos[objActual].mods[modActual].inicio['inicio'] = cont
    else:
        dirProc[modActual].inicio['inicio'] = cont

def p_modbloq(p):
    '''modbloq  :   estatuto modbloq
                |   return modbloq
                |   varcte modbloq
                |'''

#####SEMÁNTICA DE MODULO
def p_semCreaMod(p):
    'semCreaMod :'
    #dirProc.append(DirProc(p[-1], modRet, []))
    global modActual, objActual, cont
    if objActual is not None:
        objetos[objActual].mods[p[-1]] = DirProc(modRet, {}, {}, {})
        modActual = p[-1]
        #print(objetos)
    else:
        modActual = p[-1]
    #print(modActual)
        dirProc[p[-1]] = DirProc(modRet, {}, {}, {})
    #print(dirProc)

#VARCTE
def p_varcte(p):
    '''varcte   :   otrasconst
                |   cteid'''

def p_cteid(p):
    'cteid  :   IDENTI funcdimobj'
    #print(objActual, p[1])
    
def p_funcdimobj(p):
    '''funcdimobj   :   metodoCall
                    |   dimension
                    |   PUNTO IDENTI llamaObjeto limpia
                    |   foundID''' #dimobjcall

def p_limpia(p):
    'limpia     :   '
    global objActual
    objActual = None

def p_metodoCall(p):
    'metodoCall     :   LPAREN generaERA llamaParam RPAREN resetPARAM SEMCOL'
    global objActual

def p_llamaObjeto(p):
    '''llamaObjeto      :   foundID
                        |   metodoCall'''
    global objActual, modActual, MemObjeto, varObjeto
    if p[-2] is ".":
        objActual = dirProc[modActual].vars[p[-3]].type
        if p[-1] in objetos[objActual].vars:
            tipoEs = objetos[objActual].vars[p[-1]].type
            pTipos.append(tipoEs)
            pilaO.append(varObjeto[p[-3]].int[p[-1]])

def p_llamaParam(p):
    '''llamaParam   :   exp generaPARAM mascall
                    |'''

def p_mascall(p):
    '''mascall  :   COMMA exp generaPARAM mascall
                |'''

def p_generaERA(p):
    'generaERA    :    '
    global cont, modActual, modSiguiente, objActual
    print(objActual, modActual, modSiguiente)
    if p[-3] is not '.':
        cuad.append(Cuadruplo(cont, 19, -1, -1, p[-2]))
        modSiguiente = p[-2]
        cont += 1
    else:
        cuad.append(Cuadruplo(cont, 19, -1, -1, p[-2]))
        modSiguiente = p[-2]
        #Hace que el método de objeto y el objeto estén sincronizados
        objActual = dirProc[modActual].vars[p[-4]].type
        cont += 1
    print(modSiguiente)

def p_generaPARAM(p):
    'generaPARAM    :   '
    global cont, modParams
    oper1 = pilaO.pop()
    tipo = pTipos.pop()
    cuad.append(Cuadruplo(cont, 21, oper1,  -1, "param%s" % modParams))
    cont += 1
    modParams += 1

def p_resetPARAM(p):
    'resetPARAM     :   '
    global modParams, modActual, cont, modSiguiente, objActual, retOp, retTyp
    modParams = 1
    if objActual is not None:
        if modSiguiente in objetos[objActual].mods:
            cuad.append(Cuadruplo(cont, 20, -1, -1, objetos[objActual].mods[modSiguiente].inicio['inicio']))
    elif modActual in dirProc:
        cuad.append(Cuadruplo(cont, 20, -1, -1, dirProc[modSiguiente].inicio['inicio']))
    if retOp is not '':
        pilaO.append(retOp)
        pTipos.append(retTyp)
        retOp = retTyp = ''
    cont += 1

def p_otrasconst(p):
    '''otrasconst   :   CONFLO foundNUMFLO
                    |   CONINT foundNUMINT
                    |   conbol
                    |   CONSTR foundSTR'''


def p_foundNUMINT(p):
    'foundNUMINT   :'
    global MemConstINT, MemConstanteINTOffset, MemConstanteINTCont, modActual
    pTipos.append(0)
    if p[-1] in MemConstante.int:
        pilaO.append(MemConstante.int[p[-1]])
    elif MemConstanteINTOffset  < 2500:
        MemConstante.int[p[-1]] = MemConstanteINTCont + MemConstanteINTOffset
        pilaO.append(MemConstante.int[p[-1]])
        MemConstanteINTOffset += 1
    else:
        sys.exit("Demasiadas constantes enteras!!")

def p_foundNUMFLO(p):
    'foundNUMFLO    :'
    global MemConstanteFLOOffset, MemConstanteFLOCont
    pTipos.append(1)
    if p[-1] in MemConstante.float:
        pilaO.append(MemConstante.float[p[-1]])
    elif MemConstanteFLOOffset < 2500:
        MemConstante.float[p[-1]] = MemConstanteFLOCont + MemConstanteFLOOffset
        pilaO.append(MemConstante.float[p[-1]])
        MemConstanteFLOOffset += 1
    else:
        sys.exit("Demasiadas constantes flotantes")

def p_foundSTR(p):
    'foundSTR   :'
    global MemConstanteSTRCont, MemConstanteSTROffset
    pTipos.append(3)
    if p[-1] in MemConstante.str:
        pilaO.append(MemConstante.str[p[-1]])
    elif MemConstanteSTROffset < 2500:
        MemConstante.str[p[-1]] = MemConstanteSTRCont + MemConstanteSTROffset
        pilaO.append(MemConstante.str[p[-1]])
        MemConstanteSTROffset += 1
    else:
        sys.exit("Demasiadas constantes STRING")

def p_conbol(p):
    '''conbol   :   TRUE foundBOOL
                |   FALSE foundBOOL'''

def p_foundBOOL(p):
    'foundBOOL  :'
    global MemConstanteBOLOffset, MemConstanteBOLCont
    pTipos.append(2)
    if p[-1] in MemConstante.bool:
        pilaO.append(MemConstante.bool[p[-1]])
    elif MemConstanteBOLOffset < 2500:
        MemConstante.bool[p[-1]] = MemConstanteBOLCont + MemConstanteBOLOffset
        pilaO.append(MemConstante.bool[p[-1]])
        MemConstanteBOLOffset += 1
    else:
        sys.exit("Demasiadas constantes booleanas")

#TIPO
def p_tipo(p):
    '''tipo :   tipos
            |   IDENTI'''
    #print(p[1])
    if p[1] is not None:
        global vartype
        if p[1] in objetos:
            vartype = p[1]
        else:
            sys.exit("Objeto \"%s\" NO declarado!! Está en la línea %s" % (p[-1], p.lexer.lineno))

'''def p_isobject(p):
    'isobject   :   '
    global vartype
    if p[-1] in objetos:
        vartype = p[-1]
    else:
        sys.exit '''

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
        if(p[1] == 'int'):
            modParamType = 0
        elif(p[1] == 'float'):
            modParamType = 1
        elif(p[-1] == 'bool'):
            modParamType = 2
        elif(p[-1] == 'string'):
            modParamType = 3
    
#EXPRESION
def p_expresion(p):
    '''expresion    :   exp compara'''

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


def main(arg):
    #print(arg)
    if arg == 'c' or arg == 'r':
        #ENTRADA DE DATOS AL PARSER
        #Se toma la entrada del archivo "testcase"
        yacc.yacc()
        s = open('testcase', 'r').read()
        yacc.parse(s)
        print("\n%s\n" % dirProc)

        for cu in cuad:
            print("%s\t| %s,\t\t\t\t%s,\t\t\t\t%s,\t\t\t\t%s" % (cu.pos, cu.op, cu.oper1, cu.oper2, cu.res))
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
        #print(dirProc)

        print("\n\n")
        if arg == 'r':
            from VM import MaquinaVirtual
            
            MaquinaVirtual(cuad[0].pos, cuad[0].op, cuad[0].oper1, cuad[0].oper2, cuad[0].res)

        #for key, objetito in objetos.iteritems():
        #    print(objetos[key].vars)
        #    print("\n\n")
        #print(MemConstante)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))