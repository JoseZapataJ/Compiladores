class AFN:
	def __init__(self,inicial, final, estadosOrigen, estadoDestino, transicion, estadosPosibles):
		self.inicial = inicial
		self.final = final
		self.estadosOrigen = estadosOrigen
		self.estadoDestino = estadoDestino
		self.transicion = transicion
		self.estadosPosibles = estadosPosibles
	
	def establecer_inicial(nuevoInicial,Estados):
		if nuevoInicial in Estados:
			self.inicial=nuevoInicial
		else:
			self.inicial=self.inicial

	def establecer_finales(nuevoFinal,Estados):
		if nuevoFinal in Estados:
			self.final=nuevoFinal
		else:
			self.final=self.final

	def agregar_transicion(Origen,Destino,Simbolo):
		if Origen in estadosPosibles:
			estadosOrigen.append(Origen)
			estados_destino.append(Destino)
			transicion.append(simbolo)
	
	def guardar_en(nombre):
		archivo=open(nombre,"w")
		archivo.write("inicio:"+self.inicial+"\nfinal:"+self.final+"\n")
		for item in self.origen,self.destino,self.transiciones:
			archivo.write(origen[item]+"->"+destino[item]+","+transiciones[item]+"\n")
		archivo.close()

	def esAFN():
		if E in self.transicion:
			return true
		else:	
			return false

	def esAFD():
		if E in self.transicion:
			return false
		else:	
			return true

	def eliminar_transicion(Origen,Destino,Simbolo):
		if(self.estadosOrigen.index(Origen,Destino,Simbolo)):
			Eliminar_porIndice = self.estadosOrigen.index(Origen,Destino,Simbolo)
			self.estadosOrigen.remove(Eliminar_porIndice)

def cargar_desde(Documento):
	ListaConSaltos=[]
	listaLimpia=[]
	estadosOrigen=[]
	estadoDestino=[]
	estadosPosibles=[]
	transicion=[]

	#inicia la lectura del archivo
	with open(Documento) as automata:
		for linea in automata:
			ListaConSaltos.append(linea)
	for item in ListaConSaltos:
		listaLimpia.append((item.rstrip()))

	inicial=obtener_inicial(listaLimpia)
	final=obtener_final(listaLimpia)
	
	for linea in listaLimpia[2:]:
		linea=linea.replace("->",",")
		linea=linea.split(",") 
		estadosOrigen.append(int(linea[0]))
		estadoDestino.append(int(linea[1]))
		transicion.append(linea[2])
		estadosPosibles=list((set(estadosOrigen)))
	
	return AFN(inicial,final,estadosOrigen,estadoDestino,transicion,estadosPosibles)

def obtener_inicial(Lista):
	Inicio=Lista[0]
	inicial=int(Inicio[8:])
	return inicial

def obtener_final(Lista):
	Finales=Lista[1]
	final=int(Finales[8:])
	final=final
	return final

cargar_desde("Automata.af")	