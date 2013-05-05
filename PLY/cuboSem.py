#coding=UTF-8
#CUBO SEMÁNTICO
#MARFLE - COMPILADORES ENE-MAYO 2013
#RUBÉN ALEJANDRO VALDEZ RUIZ A00803015


'''
Tipos de datos
int     0
float   1
bool    2
string  3
ERROR   -1

OPERADORES
        +       -       *       /       <       >       !=      <=      >=      ==      =       &&      ||

'''


cuboSem = [
    [
        #INT op INT
        [0,     0,      0,      1,      2,      2,      2,      2,      2,      2,      0,      -1,     -1],
        #INT op FLOAT
        [1,     1,      1,      1,      2,      2,      2,      2,      2,      2,      -1,     -1,     -1],
        #INT op BOOL
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1],
        #INT op STRING
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1]
    ],
    [
        #FLOAT op INT
        [1,     1,      1,      1,      2,      2,      2,      2,      2,      2,      1,      -1,     -1],
        #FLOAT op FLOAT
        [1,     1,      1,      1,      2,      2,      2,      2,      2,      2,      1,      -1,     -1],
        #FLOAT op BOOL
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1],
        #FLOAT op STRING
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1]
    ],
    [
        #BOOL op INT
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1],
        #BOOL op FLOAT
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1],
        #BOOL op BOOL
        [-1,    -1,     -1,     -1,     2,      2,      2,      2,      2,      2,      2,      2,      2],
        #BOOL op STRING
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1]
    ],
    
    [
        #STRING op INT
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1],
        #STRING op FLOAT
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1],
        #STRING op BOOL
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1],
        #SRTING op STRING
        [-1,    -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1,      3,     -1,     -1]
    ]
]

#print(cuboSem)

#print(cuboSem[0][1][4])