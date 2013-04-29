#coding=UTF-8
from marfle_yacc import cuad, MemConstante, MemTemporal, MemGlobal, MemLocal, dirProc, objetos
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
stackLocal = []
stackEstado = []
#print(invMemConstSTR)
vmModActual = 'main'

def MaquinaVirtual(pos, op, oper1, oper2, res):
	global MemGlobal, MemTemporal, MemLocalINTCont, MemLocalINTOffset, MemTempBOLCont, MemTempBOLOffset


##### 		SUMA	
	if op == 0:
		operSuma1 = operSuma2 = 0
		
		#OPERADOR 1
		  ##########				ENTEROS
			#Constantes
		if 32500 <= oper1 < 35000:
			operSuma1 = invMemConstINT[oper1]
			#Temporales
		elif 22500 <= oper1 < 25000:
			operSuma1 = MemTemporal.int[oper1]
			#print(operSuma1)
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int:
				operSuma1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable NO inicializada")
		elif 12500 <= oper1 < 15000:
			operSuma1 = stackLocal[len(stackLocal) - 1].int[oper1]

		
		#OPERADOR 2
		if 32500 <= oper2 < 35000:
			operSuma2 = invMemConstINT[oper2]
		elif 22500 <= oper2 < 25000:
			operSuma2 = MemTemporal.int[oper2]
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int:
				operSuma2 = MemGlobal.int[oper2]
			else:
				sys.exit("Variable NO inicializada")
		elif 12500 <= oper2 < 15000:
			operSuma2 = stackLocal[len(stackLocal) - 1].int[oper2]
			#print(oper2)

		##########				FLOTANTES


		#print(operSuma1, operSuma2)
		try:
			MemTemporal.int[res] = operSuma1 + operSuma2
		except:
			MemTemporal.int[res] = operSuma1 + operSuma2
		
		#print(MemTemporal.int[res])

		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)

#########		RESTA
	elif op == 1:
		operResta1 = operResta2 = 0

		#OPERADOR 1
		if 32500 <= oper1 < 35000:
			operResta1 = invMemConstINT[oper1]
		elif 22500 <= 25000:
			operResta1 = MemTemporal.int[oper1]
		elif 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int:
				operResta1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			operResta2 = stackLocal[len(stackLocal) - 1].int[oper2]

		#OPERADOR 2
		if 32500 <= oper2 < 35000:
			operResta2 = invMemConstINT[oper2]
		elif 22500 <= 25000:
			operResta2 = MemTemporal.int[oper2]
		elif 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int:
				operResta2 = MemGlobal.int[oper2]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper2 < 15000:
			operResta2 = stackLocal[len(stackLocal) - 1].int[oper2]

		MemTemporal.int[res] = operResta1 - operResta2
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)

###########			PRODUCTO
	elif op == 2:
		operMult1 = operMult2 = 0

		#OPERADOR 1
		if 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operMult1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			operMult1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operMult1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operMult1 = invMemConstINT[oper1]

		#OPERADOR 2
		if 2500 <= oper2 < 5000:
			if oper1 in MemGlobal.int[oper2]:
				operMult2 = MemGlobal.int[oper2]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper2 < 15000:
			operMult2 = stackLocal[len(stackLocal) - 1].int[oper2]
		elif 22500 <= oper2 < 25000:
			operMult2 = MemTemporal.int[oper2]
		elif 32500 <= oper2 < 35000:
			operMult2 = invMemConstINT[oper2]


		##### OTROS TIPOS

		MemTemporal.int[res] = operMult1 * operMult2
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 3:
###########			DIVISION
		print("Hay DIVISION")
		operDiv1 = operDiv2 = 0
		###			ENTEROS
			###			OPERADOR 1
		if 2500 <= oper1 < 5000:
			if oper1 in MemGlobal.int[oper1]:
				operDiv1 = MemGlobal.int[oper1]
			else:
				sys.exit("Variable no inicializada")
		elif 12500 <= oper1 < 15000:
			operDiv1 = stackLocal[len(stackLocal) - 1].int[oper1]
		elif 22500 <= oper1 < 25000:
			operDiv1 = MemTemporal.int[oper1]
		elif 32500 <= oper1 < 35000:
			operDiv1 = invMemConstINT[oper1]

			###			OPERADOR 2
		if 2500 <= oper2 < 5000:
			if oper2 in MemGlobal.int[oper2]:
				operDiv2 = MemGlobal.int[oper2]
			else:
				sys.exit("Variable no inicializada")
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
			#Es entero
		if 2500 <= oper1 < 5000:
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
			#Es Entero
		if 2500 <= oper2 < 5000:
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

		if operador1 < operador2:
			MemTemporal.bool[res] = True
		else:
			MemTemporal.bool[res] = False

		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 5:
		print("Hay Mayorque")
		#OPERADOR 1
		operador1 = operador2 = 0
			#Es entero
		if 2500 <= oper1 < 5000:
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
			#Es Entero
		if 2500 <= oper2 < 5000:
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
			#Es entero
		if 2500 <= oper1 < 5000:
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
			#Es Entero
		if 2500 <= oper2 < 5000:
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
			#Es entero
		if 2500 <= oper1 < 5000:
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
			#Es Entero
		if 2500 <= oper2 < 5000:
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
			#Es entero
		if 2500 <= oper1 < 5000:
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
			#Es Entero
		if 2500 <= oper2 < 5000:
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
		print("Hay IguIgu")
		#OPERADOR 1
		operador1 = operador2 = 0
			#Es entero
		if 2500 <= oper1 < 5000:
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
			#Es Entero
		if 2500 <= oper2 < 5000:
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
		#Es una variable global entera
		if 2500 <= res < 5000:
			if res in MemGlobal.int:
				if 2500 <= oper1 < 5000:
					MemGlobal.int[res] = MemGlobal.int[oper1]
				elif 32500 <= oper1 < 35000:
					MemGlobal.int[res] = invMemConstINT[oper1]
				elif 22500 <= oper1 < 25000:
					MemGlobal.int[res] = MemTemporal.int[oper1]
			else:
				if 2500 <= oper1 < 5000:
					MemGlobal.int[res] = MemGlobal.int[oper1]
				elif 32500 <= oper1 < 35000:
					MemGlobal.int[res] = invMemConstINT[oper1]
				elif 22500 <= oper1 < 25000:
					MemGlobal.int[res] = MemTemporal.int[oper1]

		#Es una variable global Flotante
		if 5000 <= res < 7500:
			if res in MemGlobal.float:
				if 5000 <= oper1 < 7500:
					MemGlobal.float[res] = MemGlobal.float
		
		#Es una Variable global Booleana
		elif 7500 <= res < 10000:
			pass

		#Es una variable global string
		elif 10000 <= res < 12500:
			if 40000 <= oper1 < 42500:
				MemGlobal.str[res] = invMemConstSTR[oper1]

		#LOCALES
		if 12500 <= res < 15000:
			if 32500 <= oper1 < 35000:
				stackLocal[len(stackLocal) - 1].int[res] = invMemConstINT[oper1]
			elif 22500 <= oper1 < 25000:
				stackLocal[len(stackLocal) - 1].int[res] = MemTemporal.int[oper1]
			elif 12500 <= oper1 < 25000:
				stackLocal[len(stackLocal) - 1].int[res] = stackLocal[len(stackLocal) - 1].int[oper1]


		if pos < len(cuad) - 1:
			MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
		else:
			print("DONE")
	elif op == 11:
		print("Hay AND")
		#OPERADOR 1
		operador1 = operador2 = 0
			#Es entero
		if 2500 <= oper1 < 5000:
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
			#Es Entero
		if 2500 <= oper2 < 5000:
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
		print("Hay OR")
		#OPERADOR 1
		operador1 = operador2 = 0
			#Es entero
		if 2500 <= oper1 < 5000:
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
			#Es Entero
		if 2500 <= oper2 < 5000:
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

		if operador1 or operador2:
			MemTemporal.bool[res] = True
		else:
			MemTemporal.bool[res] = False

		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 13:
		print("Hay NOT") #No se usa en el producto final
	elif op == 14:	#PRINT

		#GLOBALES
		if 2500 <= res < 5000:

			print(MemGlobal.int[res])
		elif 5000 <= res < 7500:
			pass
		elif 7500 <= res < 10000:
			pass
		elif 10000 <= res < 12500:
			#pass
			print(MemGlobal.str[res])

		#LOCALES
		if 12500 <= res < 15000:
			print(stackLocal[len(stackLocal) - 1].int[res])

		#CONSTANTES
		if 32500 <= res < 35000:
			print(invMemConstINT[res])
		elif 35000 <= res < 37500:
			pass
		elif 40000 <= res < 42500:
			print(invMemConstSTR[res])

		#Temporales
		if 22500 <= res < 25000:
			print(MemTemporal.int[res])

		if pos < len(cuad) - 1:
			MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
		else:
			print("DONE")
	elif op == 15:
		print("Hay RETURN")
	elif op == 16:
		#print("Hay GOTOF")
		#print(pos)
		#print(MemTemporal.bool[oper1])
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
		if 2500 <= oper1 < 5000:
			parametro = MemGlobal.int[oper1]
			stackLocal[len(stackLocal) - 1].int[MemLocalINTCont + MemLocalINTOffset] = parametro
			MemLocalINTOffset += 1
			#print(stackLocal)
		if 22500 <= oper1 < 25000:
			parametro = MemTemporal.int[oper1]
			stackLocal[len(stackLocal) - 1].int[MemLocalINTCont + MemLocalINTOffset] = parametro
			MemLocalINTOffset += 1
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 22:
		siguienteCuad = stackEstado.pop()
		stackLocal.pop()
		#print(stackLocal)
		MaquinaVirtual(cuad[siguienteCuad].pos, cuad[siguienteCuad].op, cuad[siguienteCuad].oper1, cuad[siguienteCuad].oper2, cuad[siguienteCuad].res)
	elif op == 23:
		print("Hay READ")

