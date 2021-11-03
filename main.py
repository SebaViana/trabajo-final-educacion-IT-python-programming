import os
import time
import openpyxl
import funciones
import Pedido



f = open("registro.txt","a")
f.close()
 
f = open("registro.txt","r")
data = f.readlines()
f.close()
ans=True
while ans == True:
	print("\nBienvenido a McDowell´s\n")
	nombre_de_encargado = input("Ingrese su nombre encargad@ :")
	nombre_de_encargado = funciones.verificar_vacio(nombre_de_encargado)
	nombre_de_encargado = funciones.verificar_nombre(nombre_de_encargado)
	f = open("registro.txt","a")
	f.write("IN " + time.asctime() + " " + "encargad@ " + str(nombre_de_encargado.capitalize()) + "\n")
	f.close()
	while True:

		os.system("cls")
		tiempo = int(time.strftime('%H'))
		Saludo = funciones.saludo_tiempo(tiempo, nombre_de_encargado.capitalize())

		print("""

		1 – Ingreso de nuevo pedido
		2 – Cambio de turno
		3 – Apagar sistema

		""")
		
		opcion = input(">>>")
		if opcion == "1":
			Pedido.iniciar_menu()
			
		elif opcion == "2":
			f = open("registro.txt","a")
			f.write("OUT " + time.asctime() + " " + "encargad@ " + str(nombre_de_encargado.capitalize()) + " " + "$" + str(funciones.total_en_caja) + "\n")
			f.write("###########################################\n")
			f.close()
			break
		
		
		elif opcion == "3":
			print("Gracias por usar nuestro programa.")
			f = open("registro.txt","a")
			f.write("OUT " + time.asctime() + " " + "encargad@ " + str(nombre_de_encargado.capitalize()) + " " + "$" + str(funciones.total_en_caja) + "\n")
			f.write("###########################################\n")
			f.close()
			ans = False
			break