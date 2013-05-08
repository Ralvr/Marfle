#coding=UTF-8
from marfle_yacc import cuad, MemConstante, MemTemporal, MemGlobal, MemLocal, dirProc, objetos
import sys, re
#print(MemTemporal)

'''
##################################################################
MEMORIAS!!
Las memorias globales están en el rango de 2500 a 12499

Las memorias locales están en el rango de 12500 a 22499

Las memorias temporales están en el rango de 22500 a 32499

Las memorias constantes están en el rango de 32500 a 42499
##################################################################
'''

MemLocalINTCont = 12500
MemLocalINTLimite = 15000
MemLocalINTOffset = 0

MemTempBOLCont = 27500
MemTempBOLOffset = 0

invMemConstINT 	= 	{MemConstante.int[k] : k for k in MemConstante.int}
invMemConstSTR	=	{MemConstante.str[k] : k for k in MemConstante.str}
invMemConstFLO 	=	{MemConstante.float[k] : k for k in MemConstante.float}
invMemConstBOL	=	{MemConstante.bool[k] : k for k in MemConstante.bool}
stackLocal = []
stackEstado = []
#print(invMemConstSTR)
vmModActual = 'main'

def MaquinaVirtual(pos, op, oper1, oper2, res):
	global MemGlobal, MemTemporal, MemLocalINTCont, MemLocalINTOffset, MemTempBOLCont, MemTempBOLOffset, invMemConstFLO, invMemConstBOL


##### 		SUMA	
	if op == 0:
		operSuma1 = operSuma2 = 0
		#print(oper1, oper2, res)
		#OPERADOR 1

		#Arreglos para globales y locales
		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operSuma1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operSuma1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operSuma1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operSuma1 = MemLocal.int[destino]

		  ##########				ENTEROS
			#Constantes
		elif 32500 <= oper1 < 35000:
			operSuma1 = invMemConstINT[oper1]
			#Temporales
		elif 22500 <= oper1 < 25000:
			operSuma1 = MemTemporal.int[oper1]
			#print(operSuma1)
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int:
				operSuma1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable NO inicializada MAS")
		elif 12500 <= oper1 < 15000:
			operSuma1 = stackLocal[len(stackLocal) - 1].int[oper1]

		
		#OPERADOR 2
		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operSuma2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operSuma2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operSuma2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operSuma2 = MemLocal.int[destino]

		elif 32500 <= oper2 < 35000:
			operSuma2 = invMemConstINT[oper2]
		elif 22500 <= oper2 < 25000:
			operSuma2 = MemTemporal.int[oper2]
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int:
				operSuma2 = MemGlobal.int[oper2]
			else:
				sys.exit("Variable NO inicializada MAS")
		elif 12500 <= oper2 < 15000:
			operSuma2 = stackLocal[len(stackLocal) - 1].int[oper2]
			#print(oper2)

		##########				FLOTANTES


		
		MemTemporal.int[res] = operSuma1 + operSuma2
		
		#print(MemTemporal.int[res])

		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)

#########		RESTA
	elif op == 1:
		operResta1 = operResta2 = 0

		#OPERADOR 1

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operResta1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operResta1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operResta1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operResta1 = MemLocal.int[destino]

		elif 32500 <= oper1 < 35000:
			operResta1 = invMemConstINT[oper1]
		elif 22500 <= oper1 < 25000:
			operResta1 = MemTemporal.int[oper1]
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int:
				operResta1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada MENOS")
		elif 12500 <= oper1 < 15000:
			#print(stackLocal[len(stackLocal)-1])
			operResta1 = stackLocal[len(stackLocal) - 1].int[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operResta2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operResta2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operResta2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operResta2 = MemLocal.int[destino]

		elif 32500 <= oper2 < 35000:
			operResta2 = invMemConstINT[oper2]
		elif 22500 <= oper2 < 25000:
			operResta2 = MemTemporal.int[oper2]
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int:
				operResta2 = MemGlobal.int[oper2]
			else:
				sys.exit("Variable no inicializada MENOS")
		elif 12500 <= oper2 < 15000:
			operResta2 = stackLocal[len(stackLocal) - 1].int[oper2]

		MemTemporal.int[res] = operResta1 - operResta2
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)

###########			PRODUCTO
	elif op == 2:
		operMult1 = operMult2 = 0

		#OPERADOR 1

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operMulti1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operMulti1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operMulti1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operMulti1 = MemLocal.int[destino]

		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operMult1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada POR")
		elif 12500 <= oper1 < 15000:
			operMult1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operMult1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operMult1 = invMemConstINT[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operMulti2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operMulti2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operMulti2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operMulti2 = MemLocal.int[destino]
		
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int:
				operMult2 = MemGlobal.int[oper2]
			else:
				sys.exit("Variable no inicializada POR")
		elif 12500 <= oper2 < 15000:
			operMult2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			operMult2 = MemTemporal.int[oper2]
		elif 32500 <= oper2 < 35000:
			operMult2 = invMemConstINT[oper2]



		MemTemporal.int[res] = operMult1 * operMult2
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 3:
###########			DIVISION
		operDiv1 = operDiv2 = 0
		###			ENTEROS
		###			OPERADOR 1

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operDiv1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operDiv1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operDiv1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operDiv1 = MemLocal.int[destino]

		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operDiv1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada DIVI")
		elif 12500 <= oper1 < 15000:
			operDiv1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operDiv1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operDiv1 = invMemConstINT[oper1]

			###			OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operDiv2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operDiv2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operDiv2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operDiv2 = MemLocal.int[destino]

		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operDiv2 = MemGlobal.int[oper2]
			else:
				sys.exit("Variable no inicializada DIVI")
		elif 12500 <= oper2 < 15000:
			operDiv2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			operDiv2 = MemTemporal.int[oper2]
		elif 32500 <= oper2 < 35000:
			operDiv2 = invMemConstINT[oper2]

		MemTemporal.int[res] = operDiv1 / operDiv2
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 4:
		#print("Hay Menorque")
		#OPERADOR 1
		operador1 = operador2 = 0

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador1 = MemLocal.int[destino]

			#Es entero
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operador1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada MENQ")
		elif 12500 <= oper1 < 15000:
			operador1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operador1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operador1 = invMemConstINT[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador2 = MemLocal.int[destino]

			#Es Entero
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operador2 = MemGlobal.int[oper2]
			else:
				sys.exit("Varibale no inicializada MENQ")
		elif 12500 <= oper2 < 15000:
			operador2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			pass
		elif 32500 <= oper2 < 35000:
			operador2 = invMemConstINT[oper2]
		if operador1 < operador2:
			MemTemporal.bool[res] = True
		else:
			MemTemporal.bool[res] = False

		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 5:
		print("Hay Mayorque")
		#OPERADOR 1
		operador1 = operador2 = 0

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador1 = MemLocal.int[destino]

			#Es entero
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operador1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			operador1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operador1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operador1 = invMemConstINT[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador2 = MemLocal.int[destino]

			#Es Entero
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operador2 = MemGlobal.int[oper2]
			else:
				sys.exit("Varibale no inicializada")
		elif 12500 <= oper2 < 15000:
			operador2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			pass
		elif 32500 <= oper2 < 35000:
			operador2 = invMemConstINT[oper2]

		if operador1 > operador2:
			MemTemporal.bool[res] = True
		else:
			MemTemporal.bool[res] = False
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 6:
		print("Hay Dieferente")
		#OPERADOR 1
		operador1 = operador2 = 0

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador1 = MemLocal.int[destino]

			#Es entero
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operador1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			operador1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operador1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operador1 = invMemConstINT[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador2 = MemLocal.int[destino]

			#Es Entero
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operador2 = MemGlobal.int[oper2]
			else:
				sys.exit("Varibale no inicializada")
		elif 12500 <= oper2 < 15000:
			operador2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			pass
		elif 32500 <= oper2 < 35000:
			operador2 = invMemConstINT[oper2]

		if operador1 != operador2:
			MemTemporal.bool[res] = True
		else:
			MemTemporal.bool[res] = False
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 7:
		print("Hay MenorIgu")
		#OPERADOR 1
		operador1 = operador2 = 0

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador1 = MemLocal.int[destino]

			#Es entero
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operador1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			operador1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operador1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operador1 = invMemConstINT[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador2 = MemLocal.int[destino]

			#Es Entero
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operador2 = MemGlobal.int[oper2]
			else:
				sys.exit("Varibale no inicializada")
		elif 12500 <= oper2 < 15000:
			operador2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			pass
		elif 32500 <= oper2 < 35000:
			operador2 = invMemConstINT[oper2]

		if operador1 <= operador2:
			MemTemporal.bool[res] = True
		else:
			MemTemporal.bool[res] = False
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 8:
		print("Hay MayorIgu")
		#OPERADOR 1
		operador1 = operador2 = 0

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador1 = MemLocal.int[destino]

			#Es entero
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operador1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			operador1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operador1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operador1 = invMemConstINT[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador2 = MemLocal.int[destino]

			#Es Entero
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operador2 = MemGlobal.int[oper2]
			else:
				sys.exit("Varibale no inicializada")
		elif 12500 <= oper2 < 15000:
			operador2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			pass
		elif 32500 <= oper2 < 35000:
			operador2 = invMemConstINT[oper2]

		if operador1 >= operador2:
			MemTemporal.bool[res] = True
		else:
			MemTemporal.bool[res] = False
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 9:
		#OPERADOR 1
		operador1 = operador2 = 0

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador1 = MemLocal.int[destino]

			#Es entero
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operador1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			#print(stackLocal[len(stackLocal)-1])
			operador1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operador1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operador1 = invMemConstINT[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador2 = MemLocal.int[destino]

			#Es Entero
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operador2 = MemGlobal.int[oper2]
			else:
				sys.exit("Varibale no inicializada")
		elif 12500 <= oper2 < 15000:
			operador2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			pass
		elif 32500 <= oper2 < 35000:
			operador2 = invMemConstINT[oper2]

		if operador1 == operador2:
			MemTemporal.bool[res] = True
		else:
			MemTemporal.bool[res] = False
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 10:
		if type(res) is str:
			dirDest = int(re.search(r'\d+', res).group())
			if 22500 <= dirDest < 25000:
				#print(MemLocal.int)
				destino = MemTemporal.int[dirDest]
				#print(destino, oper1)
				if 2500 <= destino < 5000:
					if 2500 <= oper1 < 5000:
						MemGlobal.int[destino] = MemGlobal.int[oper1]
					elif 12500 <= oper1 < 15000:
						MemGlobal.int[destino] = MemLocal.int[oper1]
					elif 32500 <= oper1 < 35000:
						MemGlobal.int[destino] = invMemConstINT[oper1]
					elif 22500 <= oper1 < 25000:
						MemGlobal.int[destino] = MemTemporal.int[oper1]
				elif 5000 <= destino < 7500:
					if 5000 <= oper1 < 7500:
						MemGlobal.float[destino] = MemGlobal.float[oper1]
					elif 15000 <= oper1 < 17500:
						MemGlobal.float[destino] = MemLocal.float[oper1]
					elif 25000 <= oper1 < 27500:
						MemGlobal.float[destino] = MemTemporal.float[oper1]
					elif 35000 <= oper1 < 37500:
						MemGlobal.float[destino] = invMemConstFLO[oper1]
				elif 12500 <= destino < 15000:
					if 2500 <= oper1 < 5000:
						MemLocal.int[destino] = MemGlobal.int[oper1]
					elif 12500 <= oper1 < 15000:
						MemLocal.int[destino] = MemLocal.int[oper1]
					elif 32500 <= oper1 < 35000:
						MemLocal.int[destino] = invMemConstINT[oper1]
					elif 22500 <= oper1 < 25000:
						MemLocal.int[destino] = MemTemporal.int[oper1]
						#print(MemTemporal.int)

		#Es una variable global entera
		elif 2500 <= res < 5000:
			#if res in MemGlobal.int:
			if type(oper1) is str:
				dirDest = int(re.search(r'\d+', oper1).group())
				if 22500 <= dirDest < 25000:
					destino = MemTemporal.int[dirDest]
					oper1 = destino
			
			if 2500 <= oper1 < 5000:
				MemGlobal.int[res] = MemGlobal.int[oper1]
			elif 12500 <= oper1 < 15000:
				MemGlobal.int[res] = MemLocal.int[oper1]
			elif 32500 <= oper1 < 35000:
				MemGlobal.int[res] = invMemConstINT[oper1]
			elif 22500 <= oper1 < 25000:
				MemGlobal.int[res] = MemTemporal.int[oper1]
			'''else:
				if 2500 <= oper1 < 5000:
					MemGlobal.int[res] = MemGlobal.int[oper1]
				elif 32500 <= oper1 < 35000:
					MemGlobal.int[res] = invMemConstINT[oper1]
				elif 22500 <= oper1 < 25000:
					MemGlobal.int[res] = MemTemporal.int[oper1]'''

		#Es una variable global Flotante
		elif 5000 <= res < 7500:
			#if res in MemGlobal.float:
			if 2500 <= oper1 < 5000:
				MemGlobal.float[res] = MemGlobal.int[oper1]
			elif 12500 <= oper1 < 15000:
				MemGlobal.float[res] = MemLocal.int[oper1]
			elif 32500 <= oper1 < 35000:
				MemGlobal.float[res] = invMemConstINT[oper1]
			elif 22500 <= oper1 < 25000:
				MemGlobal.float[res] = MemTemporal.int[oper1]
			elif 5000 <= oper1 < 7500:
				MemGlobal.float[res] = MemGlobal.float[oper1]
			elif 15000 <= oper1 < 17500:
				MemGlobal.float[res] = MemLocal.float[oper1]
			elif 25000 <= oper1 < 27500:
				MemGlobal.float[res] = MemTemporal.float[oper1]
			elif 35000 <= oper1 < 37500:
				MemGlobal.float[res] = invMemConstFLO[oper1]


		
		#Es una Variable global Booleana
		elif 7500 <= res < 10000:
			pass

		#Es una variable global string
		elif 10000 <= res < 12500:
			if 40000 <= oper1 < 42500:
				MemGlobal.str[res] = invMemConstSTR[oper1]

		#LOCALES
		elif 12500 <= res < 15000:
			if 32500 <= oper1 < 35000:
				stackLocal[len(stackLocal) - 1].int[res] = invMemConstINT[oper1]
			elif 22500 <= oper1 < 25000:
				stackLocal[len(stackLocal) - 1].int[res] = MemTemporal.int[oper1]
			elif 12500 <= oper1 < 25000:
				stackLocal[len(stackLocal) - 1].int[res] = stackLocal[len(stackLocal) - 1].int[oper1]

		#Es una variable dimensionada


		if pos < len(cuad) - 1:
			MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
		else:
			print("DONE")
	elif op == 11:
		#OPERADOR 1
		operador1 = operador2 = 0

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador1 = MemLocal.int[destino]

			#Es entero
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operador1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			operador1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operador1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operador1 = invMemConstINT[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador2 = MemLocal.int[destino]

			#Es Entero
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operador2 = MemGlobal.int[oper2]
			else:
				sys.exit("Varibale no inicializada")
		elif 12500 <= oper2 < 15000:
			operador2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			pass
		elif 32500 <= oper2 < 35000:
			operador2 = invMemConstINT[oper2]

		if operador1 and operador2:
			MemTemporal.bool[res] = True
		else:
			MemTemporal.bool[res] = False

		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 12:
		#OPERADOR 1
		operador1 = operador2 = 0

		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador1 = MemLocal.int[destino]

			#Es entero
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operador1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			operador1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operador1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operador1 = invMemConstINT[oper1]

			#Es flotante
		elif 5000 <= oper1 < 7500:
			if oper1 in MemGlobal.float:
				operador1 = MemGlobal.float[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 15000 <= oper1 < 17500:
			operador1 = stackLocal[len(stackLocal) - 1].float[oper1]
		elif 25000 <= oper1 < 27500:
			operador1 = MemTemporal.float[oper1]
		elif 35000 <= oper1 < 37500:
			operador1 = invMemConstFLO[oper1]

			#Es boolean
		elif 7500 <= oper1 < 10000:
			if oper1 in MemGlobal.bool:
				operador1 = MemGlobal.bool[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 17500 <= oper1 < 20000:
			operador1 = stackLocal[len(stackLocal) -1].bool[oper1]
		elif 27500 <= oper1 < 30000:
			operador1 = MemTemporal.bool[oper1]
		elif 37500 <= oper1 < 40000:
			operador1 = invMemConstBOL[oper1]

		#OPERADOR 2

		if type(oper2) is str:
			dirDest = int(re.search(r'\d+', oper2).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					operador2 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					operador2 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					operador2 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					operador2 = MemLocal.int[destino]

			#Es Entero
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operador2 = MemGlobal.int[oper2]
			else:
				sys.exit("Varibale no inicializada")
		elif 12500 <= oper2 < 15000:
			operador2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			pass
		elif 32500 <= oper2 < 35000:
			operador2 = invMemConstINT[oper2]

			#Es flotante
		elif 5000 <= oper2 < 7500:
			if oper1 in MemGlobal.float:
				operador2 = MemGlobal.float[oper2]
			else:
				sys.exit("Variable no inicializada")
		elif 15000 <= oper2 < 17500:
			operador2 = stackLocal[len(stackLocal) - 1].float[oper2]
		elif 25000 <= oper2 < 27500:
			operador2 = MemTemporal.float[oper2]
		elif 35000 <= oper2 < 37500:
			operador2 = invMemConstFLO[oper2]

			#Es boolean
		elif 7500 <= oper2 < 10000:
			if oper2 in MemGlobal.bool:
				operador2 = MemGlobal.bool[oper2]
			else:
				sys.exit("Variable no inicializada")
		elif 17500 <= oper2 < 20000:
			operador2 = stackLocal[len(stackLocal) -1].bool[oper2]
		elif 27500 <= oper2 < 30000:
			operador2 = MemTemporal.bool[oper2]
		elif 37500 <= oper2 < 40000:
			operador2 = invMemConstBOL[oper2]

		if operador1 or operador2:
			MemTemporal.bool[res] = True
			MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
		else:
			MemTemporal.bool[res] = False
			MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
		
	elif op == 13:
		print("Hay NOT") #No se usa en el producto final
	elif op == 14:	#PRINT
		#print(MemLocal.int)
		if type(res) is str:
			dirDest = int(re.search(r'\d+', res).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int[res])
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					print(MemGlobal.int[destino])
				elif 5000 <= destino < 7500:
					print(MemGlobal.float[destino])
				elif 7500 <= destino < 10000:
					print(MemGlobal.bool[destino])
				elif 10000 <= destino < 12500:
					print(MemGlobal.str[destino])
				elif 12500 <= destino < 15000:
					print(MemLocal.int[destino])

		#GLOBALES
		elif 2500 <= res < 5000:
			print(MemGlobal.int[res])
		elif 5000 <= res < 7500:
			print(MemGlobal.float[res])
			pass
		elif 7500 <= res < 10000:
			pass
		elif 10000 <= res < 12500:
			#pass
			print(MemGlobal.str[res])

		#LOCALES
		elif 12500 <= res < 15000:
			print(stackLocal[len(stackLocal) - 1].int[res])

		#CONSTANTES
		elif 32500 <= res < 35000:
			print(invMemConstINT[res])
		elif 35000 <= res < 37500:
			pass
		elif 40000 <= res < 42500:
			print(invMemConstSTR[res])

		#Temporales
		elif 22500 <= res < 25000:
			print(MemTemporal.int[res])

		if pos < (len(cuad) - 1):
			MaquinaVirtual(cuad[(pos+1)].pos, cuad[(pos+1)].op, cuad[(pos+1)].oper1, cuad[(pos+1)].oper2, cuad[(pos+1)].res)
		else:
			print("DONE")
	elif op == 15:
		#print("Hola RETURN")
		print(stackLocal)
		MaquinaVirtual(cuad[(pos+1)].pos, cuad[(pos+1)].op, cuad[(pos+1)].oper1, cuad[(pos+1)].oper2, cuad[(pos+1)].res)
	elif op == 16:	#GOTOF
		if MemTemporal.bool[oper1] == False:
			MaquinaVirtual(cuad[res].pos, cuad[res].op, cuad[res].oper1, cuad[res].oper2, cuad[res].res)
		elif MemTemporal.bool[oper1] == True:
			MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 17:
		print("Hay GOTOV")
	elif op == 18:
		MaquinaVirtual(cuad[res].pos, cuad[res].op, cuad[res].oper1, cuad[res].oper2, cuad[res].res)
	elif op == 19:
		stackLocal.append(MemLocal)

		#print(stackLocal)
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 20:
		stackEstado.append(pos + 1)

		MaquinaVirtual(cuad[res].pos, cuad[res].op, cuad[res].oper1, cuad[res].oper2, cuad[res].res)
	elif op == 21:
		#PARAMETROS
		
		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				if 2500 <= destino < 5000:
					oper1 = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					oper1 = MemGlobal.float[destino]
				elif 12500 <= destino < 15000:
					oper1 = MemLocal.int[destino]
				elif 15000 <= destino < 17500:
					oper1 = MemLocal.int[destino]

		if 2500 <= oper1 < 5000:
			parametro = MemGlobal.int[oper1]
			stackLocal[len(stackLocal) - 1].int[MemLocalINTCont + MemLocalINTOffset] = parametro
			MemLocalINTOffset += 1
			#print(stackLocal)
		elif 12500 <= oper1 < 15000:
			parametro = stackLocal[len(stackLocal)-2].int[oper1]
			stackLocal[len(stackLocal)-1].int[MemLocalINTCont + MemLocalINTOffset] = parametro
			MemLocalINTOffset += 1
		elif 22500 <= oper1 < 25000:
			parametro = MemTemporal.int[oper1]
			stackLocal[len(stackLocal) - 1].int[MemLocalINTCont + MemLocalINTOffset] = parametro
			MemLocalINTOffset += 1
		elif 32500 <= oper1 < 35000:
			parametro = invMemConstINT[oper1]
			stackLocal[len(stackLocal)-1].int[MemLocalINTCont + MemLocalINTOffset] = parametro
			MemLocalINTOffset += 1
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 22:
		siguienteCuad = stackEstado.pop()
		print(stackLocal[len(stackLocal)-1])
		stackLocal.pop()
		if siguienteCuad < (len(cuad) - 1):
			MaquinaVirtual(cuad[siguienteCuad].pos, cuad[siguienteCuad].op, cuad[siguienteCuad].oper1, cuad[siguienteCuad].oper2, cuad[siguienteCuad].res)
		else:
			print("DONE")
	elif op == 23:
		print("Hay READ")
	elif op == 24:
		#print(MemGlobal.int)
		#print(oper1, oper2, res, invMemConstINT, MemTemporal)
		if type(oper1) is str:
			dirDest = int(re.search(r'\d+', oper1).group())
			if 22500 <= dirDest < 25000:
				#print(MemTemporal.int)
				destino = MemTemporal.int[dirDest]
				#print(MemGlobal.int)
				#print(oper1, oper2, res)
				if 2500 <= destino < 5000:
					indice = MemGlobal.int[destino]
				elif 5000 <= destino < 7500:
					if 5000 <= oper1 < 7500:
						MemGlobal.float[destino] = MemGlobal.float[oper1]
					elif 15000 <= oper1 < 17500:
						MemGlobal.float[destino] = MemLocal.float[oper1]
					elif 25000 <= oper1 < 27500:
						MemGlobal.float[destino] = MemTemporal.float[oper1]
					elif 35000 <= oper1 < 37500:
						MemGlobal.float[destino] = invMemConstFLO[oper1]
		elif 22500 <= oper1 < 25000:
			indice = MemTemporal.int[oper1]

		if indice < oper2 or indice > res:
			print(indice)
			sys.exit("Índice fuera de rango")
		else:
			MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)

