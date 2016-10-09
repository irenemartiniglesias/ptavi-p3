#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
	"""
	Clase para manejar karaoke
	"""
	def __init__ (self):
		"""
		Creamos una lista para almanenar nuestros atributos y sus valores
		"""
		self.lista = []
		self.dic = {'root-layout' : ['width', 'height', 'background-color'], 
		'region' : ['id', 'top', 'bottom', 'left', 'right'], 'img' : ['src',
		'region', 'begin', 'dur'], 'audio' : ['src', 'begin', 'dur'], 
		'textstream' : ['src', 'region']}

	def startElement (self, name, atrrs):
		"""
		Método para abrir etiqueta y almacenar su contenido
		"""
		if name in self.dic:
			dic_atributos = {}
			for valor in self.dic[name]:
				dic_atributos[valor] = atrrs.get(valor, "")
			dic_etiquetas= {name : dic_atributos}
			self.lista.append(dic_etiquetas)

	def get_tags(self):
		return self.lista


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
