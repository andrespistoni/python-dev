# -*- coding: utf-8 -*-
#############################
import sys, os
sys.path.append("..")

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from graficas.principal import *

class Principal(QMainWindow):
	"""docstring for Cnsesion"""
	def __init__(self, parent=None):
		super(Principal, self).__init__(parent=parent)

		self.au = Sinergia()
		self.au.show()

		# self.permiso()

		self.au.sal.mouseReleaseEvent = self.s
		self.au.minx.mouseReleaseEvent = self.m

###########################################
	def s(self, _):
		''' Metodo para cerrar el formulario '''
		self.au.close()
###########################################
	def m(self, _):
		''' Metodo para minimizar el formulario '''
		if not self.au.isMinimized():
			self.au.showMinimized()
		else:
			self.au.setWindowState(Qt.WindowNoState)
###########################################
	def per(self):
		pass

################################################
# if __name__ == "__main__":
# 	app = QApplication(sys.argv)
# 	ap = Principal()
# 	#ap.show()
# 	sys.exit(app.exec_())