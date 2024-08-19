from django.shortcuts import render
from djangoScrapingIds.webScraping import WebScraping
import re

def validacionInput(idCategoria,tipoNavegador,tipoUrl):
	pattern  = "^(CATG)?([0-9]{4,5})$"
	idHijo=idCategoria.strip()
	arrayMsnVacio = []
	arrayMsnValidError = []
	#print('inicioooo')
	#print(len(idHijo))
	if len(idHijo) < 10 :
		result = re.match(pattern, idHijo)
		if result :
			deeplink = []
			categoriasOk = []
			categoriasOk.append(idHijo)
			#print(categoriasOk)
			deeplink = initWebScraping(categoriasOk,[],tipoNavegador,tipoUrl)
			#Caso: Se ingreso un ID correcto
			return deeplink
		else:
			#Caso: Se ingresó un valor vacío o un valor menor a 9 digitos
			arrayMsnError = ["El ID "+idHijo+" ingresado no corresponde con la nomenclatura (CATG18927) de una categoría","error-field"]
			return (arrayMsnError,arrayMsnVacio,arrayMsnValidError)
	else:
		existeCondicionArray = re.search(',', idHijo)
		if existeCondicionArray:
			idHijoLista = idHijo.split(',')
			categoriasOk = []
			categoriasNok = []
			categoriasNokString = ''
			for i in range(len(idHijoLista)):
				idHijo = idHijoLista[i].strip()
				resultItem = re.match(pattern, idHijo)
				if resultItem and len(idHijo)==9 :
					categoriasOk.append(idHijo)
				else:
					categoriasNok.append(idHijo)
			if len(categoriasOk) > 0:
				if len(categoriasNok) > 0:
					categoriasNokString = ",".join(categoriasNok)
					arrayMsnValidError = [categoriasNokString,"validation-field"]
					#return (arrayMsnError,arrayMsnVacio)
				
				deeplink = initWebScraping(categoriasOk,arrayMsnValidError,tipoNavegador,tipoUrl)
				return deeplink
			else:
				#Caso: Se ingresó un valor mayor a 10 digitos con comas sin formato
				arrayMsnError = ["La lista de IDs ingresados no tienen el formato correcto (CATG18927,CATG18937,...)","error-field"]
				return (arrayMsnError,arrayMsnVacio,arrayMsnValidError)
		else:
			#Caso: Se ingresó un valor mayor a 10 digitos sin comas
			arrayMsnError = ["La lista de IDs ingresados deben estar separados por comas (CATG18927,CATG18937,...)","error-field"]
			return (arrayMsnError,arrayMsnVacio,arrayMsnValidError)
		

#Método de invocación a la clase principal
def initWebScraping(idHijo=[],arrayMsnValidError=[],tipoNavegador='',tipoUrl=''):
	web = WebScraping(tipoNavegador)
	arrayRespuesta = web.execute(idHijo,tipoUrl)
	arrayMsnExit = []
	arrayMsnNoExit = []
	if (len(arrayRespuesta[1]) > 0):
		arrayRespuestaNOEXT = arrayRespuesta[1]
		categoriasNOEXITString = ",".join(arrayRespuestaNOEXT)
		arrayMsnNoExit = [categoriasNOEXITString,"no-exit-field"]
	if (len(arrayRespuesta[0]) > 0):
		arrayRespuestaOK = arrayRespuesta[0]
		categoriasOKString = "".join(arrayRespuestaOK)
		arrayMsnExit = [categoriasOKString,"exit-field"]
	
	return (arrayMsnExit,arrayMsnNoExit,arrayMsnValidError)