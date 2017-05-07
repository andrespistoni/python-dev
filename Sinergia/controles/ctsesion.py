# -*- coding: utf-8 -*-
#############################
import sys, os, time
import hashlib
sys.path.append("..")

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# #########################################
from bd.bdfireb import *
from graficas.inicio import *

from controles.ctprincipal import *

# #########################################
class Inicio(QMainWindow):
	"""docstring for Cnsesion"""
	def __init__(self, parent=None):
		super(Inicio, self).__init__(parent=parent)

		# help(entrar)
		self.ui = Entrar()
		self.ui.show()
		self.centrado()
		# ############################
		self.ui.borrar.clicked.connect(self.limpiar)
		self.ui.entrar.clicked.connect(self.entrar)

		self.ui.sal.mouseReleaseEvent = self.salir
		self.ui.minx.mouseReleaseEvent = self.min

	def centrado(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
# #######################################
	def limpiar(self):
		''' Metodo para limpiar las entradas del formulario '''
		self.ui.ncor.clear()
		self.ui.ncont.clear()
###############################################
	def entrar(self):
		''' 
		Metodo que valida que el correo o nombre sean validos y sean los registrados en la base de datos 
		
		'''	
		a = self.ui.ncor.text()
		if len(a.strip()) == 0:
			self.ui.error.setText('Campo A Vacio ?')
		else:
			sql = ("select * from personal where nombre = '{0}' or correo = '{1}' ").format(a, a)
			self.datos = conectar(sql)
			# print(self.datos[0][0])
			if not self.datos:
				self.ui.error.setText('Dato no disponible sigue intentando ??')
			else:
				self.contra()
				# contra(self)
###################################################
	def contra(self):
		''' 
		Metodo que valida que la contraseña sea valida y sea la registrada en la base de datos 
		'''
		b = self.ui.ncont.text()
		if len(b.strip()) == 0:
			self.ui.error.setText('Campo B Vacio ?')
		else:
			cifrado = hashlib.sha1(b.encode('utf-8'))
			if cifrado.hexdigest() == self.datos[0][8]:
				
				QMessageBox.information(self, 'Bienvenido', 'En un momento entraras')
				# self.ui.error.setText('Bienvenido... en un momento entraras')
				self.acceso()
			else:
				self.ui.error.setText('Dato no disponible sigue intentando ??')
###################################################
	def acceso(self):
		# time.sleep(10)
		self.ui.close()
		self.pt = Principal()
		foto = self.datos[0][7]
		nombre = self.datos[0][1].capitalize()
		ape = self.datos[0][2].capitalize()
		correo = self.datos[0][3]
		rol = self.datos[0][9]
		if rol == 1:
			rol = 'Administrador'
		else:
			rol = 'Empleado'

		self.pt.au.foto.setText('Todavia \n no hay foto' + '\n' + str(foto))
		self.pt.au.nom.setText('Nombre:  '  + nombre + '  ' + ape)
		self.pt.au.corr.setText('Correo:  '  + correo)
		self.pt.au.niv.setText(str('Nivel:  '  + rol))

#################################################
	def salir(self, _):
		''' Metodo para cerrar el formulario '''
		self.ui.close()
		# sys.exit()
##################################################
	def min(self, _):
		''' Metodo para minimizar el formulario '''
		if not self.ui.isMinimized():
			self.ui.showMinimized()
		else:
			self.ui.setWindowState(Qt.WindowNoState)

# if __name__ == "__main__":
# 	app = QApplication(sys.argv)
# 	ap = Inicio()
# 	#ap.show()
# 	sys.exit(app.exec_())