from prettytable import PrettyTable
import pandas as pd
import texttable as tt

class ll1:
	def __init__(self,archivo):
		gramatica=self.cargarDesde(archivo)
		self.conjuntoPrimeros=[]
		self.conjuntoSiguiente=[]
		self.terminales=[]
		self.noTerminales=[]
		self.obtenerTerminales(gramatica)
		self.obtenerNoTerminales(gramatica)
		self.obtenerPrimeros(gramatica)
		self.construirTabla()	
		
	def cargarDesde(self,documento):
		listaSaltos=[]
		listaLimpia=[]
		#inicia la lectura del archivo
		with open(documento) as automata:
			for linea in automata:
				listaSaltos.append(linea)
		for item in listaSaltos:#limpiamos los saltos de linea y los asignamos a una lista limpia
			listaLimpia.append((item.rstrip()))
		return(listaLimpia)

	def obtenerTerminales(self,gramatica):
		self.terminales.append(" ")
		for produccion in gramatica:
			for letra in produccion[3:]:
				if letra.islower() and letra not in self.terminales:
					self.terminales.append(letra)
		self.terminales.append("$")

	def obtenerNoTerminales(self, gramatica):
		for produccion in gramatica:
			if produccion[0] not in self.noTerminales:
				self.noTerminales.append(produccion[0])

	def obtenerPrimeros(self, gramatica):	
		primeros=[]	
		pendientes=[]
		vueltas=0
		for produccion in gramatica:
			elementoIzq=produccion[0]
			elementoDer=produccion[3]
			if elementoDer.islower():
				primeros.append(elementoIzq+","+elementoDer)
			else:
				pendientes.append(elementoIzq+","+elementoDer)
		while vueltas <= len(pendientes):
			for item1 in pendientes:
				for item2 in primeros:
					if item1[2]==item2[0]: 	
						primeros.append(item1[0]+","+item2[2])		
						vueltas+=1
		self.conjuntoPrimeros=pd.unique(primeros)
		print(self.conjuntoPrimeros)

	def construirTabla(self):
		filas=[]
		for item in self.noTerminales:
			for item1 in self.terminales[1:]:	
				letra=[]
				cadena= item+","+item1	
				if cadena in self.conjuntoPrimeros:
					letra.append(cadena)
					filas.append(letra)
		print(self.terminales)
		
		tabla=tt.Texttable()
		cabecera=self.terminales
		tabla.header(cabecera)
		for item in cabecera:
			print(item)
		
		for columna in zip(columnas):
			tabla.add_row(columna)
		s=tabla.draw()
		print(s)
			
lexer=ll1("gramatica.txt")