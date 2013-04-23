#coding=UTF-8
from marfle_yacc import cuad, MemConstante, MemTemporal, MemGlobal, MemLocal, dirProc, objetos
#print(MemTemporal)

MemLocalINTCont = 22500
MemLocalINTLimite = 25000
MemLocalINTOffset = 0

invMemConstINT 	= 	{MemConstante.int[k] : k for k in MemConstante.int}
invMemConstSTR	=	{MemConstante.str[k] : k for k in MemConstante.str}
stackLocal = []
stackEstado = []
#print(invMemConstSTR)
vmModActual = 'main'

def MaquinaVirtual(pos, op, oper1, oper2, res):
	global MemGlobal
	if op == 0:
		operSuma1 = operSuma2 = 0
		
		#OPERADOR 1
		if 32500 <= oper1 < 35000:
			operSuma1 = invMemConstINT[oper1]
			#MEter elif con los otros tipos que aplican
		elif 22500 <= oper1 < 25000:
			operSuma1 = MemTemporal.int[oper1]
		
		#OPERADOR 2
		if 32500 <= oper2 < 35000:
			operSuma2 = invMemConstINT[oper2]
		elif 22500 <= oper2 < 25000:
			operSuma2 = MemTemporal.int[oper2]

		MemTemporal.int[res] = operSuma1 + operSuma2

		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 1:
		operResta1 = operResta2 = 0

		#OPERADOR 1
		if 32500 <= oper1 < 35000:
			operResta1 = invMemConstINT[oper1]
		elif 22500 <= 25000:
			operResta1 = MemTemporal.int[oper1]

		#OPERADOR 2
		if 32500 <= oper2 < 35000:
			operResta2 = invMemConstINT[oper2]
		elif 22500 <= 25000:
			operResta2 = MemTemporal.int[oper2]

		MemTemporal.int[res] = operResta1 - operResta2
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 2:
		print("Hay PRODUCTO")
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 3:
		print("Hay DIVISION")
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 4:
		print("Hay Mayorque")
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 5:
		print("Hay Menoirque")
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 6:
		print("Hay Dieferente")
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 7:
		print("Hay MenorIgu")
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 8:
		print("Hay MayorIgu")
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 9:
		print("Hay IguIgu")
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 10:
		#Es una variable global entera
		if 2500 <= res < 5000:
			if res in MemGlobal.int:
				if 32500 <= oper1 < 35000:
					MemGlobal.int[res] = invMemConstINT[oper1]
				elif 22500 <= oper1 < 25000:
					MemGlobal.int[res] = MemTemporal.int[oper1]
			else:
				if 32500 <= oper1 < 35000:
					MemGlobal.int[res] = invMemConstINT[oper1]
				elif 22500 <= oper1 < 25000:
					MemGlobal.int[res] = MemTemporal.int[oper1]

		#Es una variable global Flotante
		if 5000 <= res < 7500:
			pass
		
		#Es una Variable global Booleana
		elif 7500 <= res < 10000:
			pass

		#Es una variable global string
		elif 10000 <= res < 12500:
			if 40000 <= oper1 < 42500:
				MemGlobal.str[res] = invMemConstSTR[oper1]


		if pos < len(cuad) - 1:
			MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
		else:
			print("DONE")
	elif op == 11:
		print("Hay AND")
	elif op == 12:
		print("Hay OR")
	elif op == 13:
		print("Hay NOT")
	elif op == 14:

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
		if 22500 <= res < 25000:
			print(stackLocal[len(stackLocal) - 1].int[res])

		#CONSTANTES
		if 32500 <= res < 35000:
			print(invMemConstINT[res])
		elif 35000 <= res < 37500:
			pass
		elif 40000 <= res < 42500:
			print(invMemConstSTR[res])

		if pos < len(cuad) - 1:
			MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
		else:
			print("DONE")
	elif op == 15:
		print("Hay RETURN")
	elif op == 16:
		print("Hay GOTOF")
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
			#print(stackLocal)
		MaquinaVirtual(cuad[pos+1].pos, cuad[pos+1].op, cuad[pos+1].oper1, cuad[pos+1].oper2, cuad[pos+1].res)
	elif op == 22:
		siguienteCuad = stackEstado.pop()
		stackLocal.pop()
		#print(stackLocal)
		MaquinaVirtual(cuad[siguienteCuad].pos, cuad[siguienteCuad].op, cuad[siguienteCuad].oper1, cuad[siguienteCuad].oper2, cuad[siguienteCuad].res)
	elif op == 23:
		print("Hay READ")

