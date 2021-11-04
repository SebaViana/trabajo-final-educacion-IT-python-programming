total_en_caja = 2000

def verificar_vacio(dato):
	while dato == "" or dato.isspace():
		print("Error, valor vacío.")
		dato = input("Ingrese nuevamente: ")
	return dato
 
def convertir(valor):
	while isinstance(valor, int) == False:
		try:
			valor = int(valor)
		except ValueError:
			print("Lo ingresado no es un número entero.")
			valor = input("Ingrese nuevamente: ")
	return valor
 
def verif_vuelto(precio, pago):
	while precio > pago:
		print("Error el pago debe ser mayor al importe.")
		pago = input("Ingrese nuevamente el pago: ")
		pago = verificar_vacio(pago)
		pago = convertir(pago)
	return pago


def saludo_tiempo(tiempo, nombre_de_encargado):
	if tiempo >= 6 and tiempo <= 12:
		print("Buenos días",nombre_de_encargado, "😎")
	elif tiempo > 12 and tiempo <= 18:
		print("Buenas tardes", nombre_de_encargado, "😎")
	else:
		print("Buenas noches",nombre_de_encargado, "😎")


def verificar_nombre(dato):
	while not all(x.isalpha() or x == " " for x in dato):
		print("Error, nombre invalido.")
		dato = input("Ingrese el nombre nuevamente: ")
	return dato

def verificar_si_no(valor):
	while not valor == "s" or valor == "n":
		print("La respuesta debe ser 's' o 'n'")
		valor = input(">>> ")
		valor = valor.lower()
	else:
		pass
	return valor