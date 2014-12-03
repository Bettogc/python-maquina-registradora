#-*- coding: utf-8 -*- 
# -*- coding: 850 -*-
import os
menur = True
prod_bodega = {}

#****************************************************************************************
#********************************* Sub Menú Caja Registradora ***************************
#****************************************************************************************
def menucaja():
	# CONTENIDO DEL MENÚ CAJA (OPCION 2 DEL MENU PRINCIPAL)...............................
	print "======================================================================"
	print u"\t\t\t\tSe Encuentra en Caja Registradora"
	print "======================================================================"
	print " "
	print u"Bienvenido(a)... A Caja"
	print " "
	print u"¿Qué desea hacer?"
	print " "
	print "1. Comprar"
	print "2. Facturar"
	print "3. Regresar al Menú Principal "
	print " "
	# INGRESO DE OPCIONES DENTRO DEL MENU CAJA............................................
	num_menur1 = raw_input("Ingrese Número de Opción: ")
	print " "
	# REDIRECCIONAMIENTOS ................................................................
	if num_menur1 == "1":
		os.system('clear')
		carrito()
	elif num_menur1 == "2":
		os.system('clear')
		factura()
	elif num_menur1 == "3":
		os.system('clear')
		menuprincipal()
	else:
		os.system('clear')
		print "Número fuera de rango, por favor vuelva a intentarlo"
		menucaja()
#****************************************************************************************
#******************************* Carrito de Compras *********************************
#****************************************************************************************
def carrito():
	# CONTENIDO DE LA OPCION COMPRAR (OPCION1 DEL MENU CAJA)..............................
	print " "
	print "======================================================================"
	print u"\t\tAgregue Productos a su Carrito de Compras"
	print "======================================================================"
	print ""
	subtotal = 0
	# VALIDACION DE PRODUCTOS EXISTENTES..................................................
	if len(prod_bodega)>0:
		value2=True
		while value2==True:
			# FOR PARA RECORRER EL DICCIONARIO E IMPRIMIR ELEMENTOS.......................
			for i in prod_bodega:
				print "Productos Disponibles: ", prod_bodega
				print " "
				nompro=raw_input("Producto a Llevar: ")
				print " "
				# VALIDACION DEL PRODUCTO SI EXISTE O NO..................................
				for elemento in prod_bodega:
					if elemento==nompro:
						cantidad=input("Cantidad Unitaria a comprar: ")
						print " "
						# ASIGNACION DE VARIABLES (CANTIDAD DE PRODUCTO POR PRECIO)
						sb=cantidad*prod_bodega[elemento]
						# ASIGNACION DE VARIABLES (CONTADOR MAS SB), VARIABLE GLOBAL
						subtotal = subtotal + sb
						print "*****%s Cant: %s Subtotal: Q.%s "%(elemento, cantidad,subtotal )
						print " "
						value3=True
						# ELECCION DE PRODUCTO NUEVAMENTE.................................
						while value3==True:
							seguir=raw_input("desea elegir otro articulo SI/NO: ")
							print " "
							if seguir.lower()=="si":
								os.system('clear')
								value2=True
								value3=False
							elif seguir.lower()=="no":
								value2 = False
								value3 = False
								print " "
								os.system('clear')
							else:
								print "opcion invalida"
								print " "
								value3=True
		else:
			factura(subtotal)
	else:
		print " "
		print "¿¡Qué!, ya se va?, no ha comprado nada aún, talvés es porque el Gerente no ha comprado productos para la tienda. "
		print " "

#****************************************************************************************
#********************************** Facturación *****************************************
#****************************************************************************************
def factura(compragen):
	value2=True
	cliente = raw_input("Nombre del Comprador: ")
	nit = raw_input("NIT: ")
	# CONTENIDO DE LA OPCION FACTURAR (OPCION 2 DEL MENU CAJA).............................
	print " "
	print "*. Gold"
	print "*. Silver"
	print "*. Presione cualquier tecla si no posee ninguna de las anteriores: "
	# VALIDACION PARA TARJETA CLIENTE......................................................
	while value2==True:
		tarcliente=raw_input("Posee tarjeta de Miembro? ¿Cuál?: ")
		print " "
		# TARJETA GOLD Y PROCEDIMIENTO....................................................
		if tarcliente.lower()=="gold":
			print "El Sr.(a): " + cliente +" posee tarjeta tipo: "+ tarcliente+ " por lo cual obtiene el 5%. de DESCUENTO en todas sus compras"
			print " "
			print "El Subtotal de la factura sin iva es Q.%s"%(compragen)
			iva = (compragen*0.12)
			descuento = (compragen*0.05)
			totalcompra = compragen + iva - descuento
			print " "
			print "Debe: %s"%(totalcompra)
			print "__________________________"
			print "__________________________"
			print " "
			efectivo = input("Cantidad de Pago en Efectivo: ")
			os.system('clear')
			print " "
			cambio = efectivo - compragen
			print "__________________________"
			print "__________________________"
			print " "
			print "NOMBRE: %s"%(cliente)
			print "NIT: %s"%(nit)
			print "__________________________"
			print ("Precio       %.2f\t") % compragen
			print ("IVA          %.2f\t") % iva
			print ("Total        %.2f\t") % totalcompra
			print ("Efectivo     %.2f\t") % efectivo
			print "__________________________"
			print "Cambio:   %s"%(cambio)
			break
		# TARJETA SILVER Y PROCEDIMIENTO..................................................
		elif tarcliente.lower()=="silver":
			print "El Sr.(a): " + cliente +" posee tarjeta tipo: "+ tarcliente+ " por lo cual obtiene el 2%. de DESCUENTO en todas sus compras"
			print " "
			print "El Subtotal de la factura sin iva es Q.%s"%(compragen)
			iva = (compragen*0.12)
			descuento = (compragen*0.02)
			totalcompra = compragen + iva - descuento
			print " "
			print "Debe: %s"%(totalcompra)
			print "__________________________"
			print "__________________________"
			print " "
			efectivo = input("Cantidad de Pago en Efectivo: ")
			os.system('clear')
			print " "
			cambio = efectivo - compragen
			print "__________________________"
			print "__________________________"
			print " "
			print "NOMBRE: %s"%(cliente)
			print "NIT: %s"%(nit)
			print "__________________________"
			print ("Precio       %.2f\t") % compragen
			print ("IVA          %.2f\t") % iva
			print ("Total        %.2f\t") % totalcompra
			print ("Efectivo     %.2f\t") % efectivo
			print "__________________________"
			print "Cambio:   %s"%(cambio)
			break
		# NINGUNA TARJETA Y PROCEDIMIENTO
		else:
			print "El Sr.(a): " + cliente +" no posee tarjeta de ningún tipo por lo que no obtiene el 5%. de DESCUENTO en todas sus compras"
			print " "
			print "El Subtotal de la factura sin iva es Q.%s"%(compragen)
			iva = (compragen*0.12)
			totalcompra = compragen + iva
			print "Debe: %s"%(totalcompra)
			print "__________________________"
			efectivo = input("Efectivo: ")
			cambio = efectivo - compragen
			print cliente
			print nit
			print "__________________________"
			print ("Precio       %.2f\t") % compragen
			print ("IVA          %.2f\t") % iva
			print ("Total        %.2f\t") % totalcompra
			print ("Efectivo     %.2f\t") % efectivo
			print "__________________________"
			print "Cambio:   %s"%(cambio)
			break
	print"Vuelva Pronto!"

#****************************************************************************************
#************************** Sub Menú para Opción Gerencia *******************************
#****************************************************************************************

def menugerencia():
	# CONTENIDO DEL MENU GERENCIA (OPCION 1 DEL MENU GENERAL)............................
	print "======================================================================"
	print u"\t\t\t\tMenú Gerencia"
	print "======================================================================"
	print " "
	print u"Bienvenido Lic. Edgar Pérez"
	print " "
	print u"¿Qué desea hacer?"
	print " "
	print "1. Ingreso de Productos"
	print "2. Regresar al Menú Principal:"
	print " "
	num_menur1 = raw_input("Ingrese Número de Opción: ")
	print " "
	# VALIDACION DENTRO DEL MENU PARA REDIRECCIONAR.......................................
	if num_menur1 == "1":
		os.system('clear')
		ingprod()
	elif num_menur1 =="2":
		os.system('clear')
		menuprincipal()
	else:
		print "Número fuera de rango"
		os.system('clear')
		menugerencia()


#****************************************************************************************
#************************** Sub Sub Menú para Opción Ingreso de Productos ***************
#****************************************************************************************
def ingprod():
	# CONTENIDO DE INGRESO DE PRODUCTO (OPCION 1 DEL MENU GERENCIA)........................
	print "======================================================================"
	print u"Bienvenido Nuevamente a Seleccionado la Opción de Ingreso de Productos"
	print "======================================================================"
	value1=True
	# VALIDACION DE INGRESO DE PRODUCTO A LA TIENDA.......................................
	while value1==True:
		print " "
		opcion =raw_input("Desea ingresar un producto SI/NO: ")
		print " "
		try:
			if opcion.isalpha()==True:
				if opcion.lower()=="si":
					print " "
					nompro=raw_input("Ingrese Producto: ")
					prepro=input("Precio Unitario: ")
					print " "
					# ASIGNA VALOR A UNA CLAVE............................................
					prod_bodega[nompro]=prepro
				elif opcion.lower()=="no":
					value1=False
					os.system('clear')
				else:
					print u"Lo sentimos, opciones válidas 'si/no'; intentelo nuevamente"
			else:
				print u"Lo sentimos, no acepta números"
		except:
			value1=True
	# IMPRESION DE PRODUCTOS.............................................................
	print "Los Productos en Existencia son: "
	print " "
	for i in prod_bodega:
		print i,"Q.",prod_bodega[i]
		print " "

#****************************************************************************************
#************************** Menú Principal **********************************************
#****************************************************************************************
def menuprincipal():
	# CONTENIDO DE INGRESO DEL MENU PRINCIPAL............................................
	while menur == True:
		print " "
		print "\t\t\tBienvenido a 'Super Tienda S.A.'"
		print " "
		print u"Elige una opción"
		print " "
		print "1. Gerencia"
		print "2. Caja"
		print " "
		num_menur = raw_input("Ingrese Número de Opción: ")
		print " "
		# VALIDACIONES Y REDIRECCIONAMIENTOS DENTRO DEL PROGRAMA.........................
		if num_menur == "1":
			os.system('clear')
			menugerencia()
		elif num_menur =="2":
			os.system('clear')
			menucaja()
		else:
			os.system('clear')
			print "Número fuera de Rango, Por Favor Vuelva a Intentarlo"
			print " "
menuprincipal()