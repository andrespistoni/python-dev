# -*- coding: utf-8 -*-
#############################
import sys, os


# sys.path.append("..")

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# from graficas import *
from controles.ctsesion import *
# from ctsesion import Inicio
# from controles import Principal

class Master(QMainWindow):

	def __init__(self, parent=None):
		super(Master, self).__init__(parent=parent)
		self.ui = Inicio()



# #########################################
if __name__ == "__main__":
	app = QApplication(sys.argv)
	ap = Master()
	#ap.show()
	sys.exit(app.exec_())