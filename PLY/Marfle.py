#coding=UTF-8
import marfle_yacc
import sys

if len(sys.argv) > 1:
	marfle_yacc.main(sys.argv[1])
else:
	sys.exit("\nNo se encontró parámetro.\nMarfle corre con el parámetro 'c' para compilar solamente, y el parámetro 'r' para compilar y ejecutar.\n")