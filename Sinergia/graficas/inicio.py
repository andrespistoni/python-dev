# -*- coding: utf-8 -*-

#############################
import sys
sys.path.append("..")

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from ajustes import mg

class Entrar(QWidget):
	def __init__(self):
		super(Entrar, self).__init__()
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)


		self.resize(615, 471)
		font = QFont()
		font.setFamily("Raleway Thin")
		font.setPointSize(18)
		font.setItalic(True)
		self.setFont(font)

		self.grid1 = QGridLayout(self)
		self.grid1.setContentsMargins(-1, 1, -1, -1)
		self.grid1.setObjectName("grid1")

		self.lobox = QGroupBox()
		self.lobox.setAlignment(Qt.AlignCenter)
		self.lobox.setObjectName("lobox")
		self.grid2 = QGridLayout(self.lobox)
		self.grid2.setObjectName("grid2")

		self.mr1 = QFrame(self.lobox)
		self.mr1.setMaximumSize(QSize(16777215, 70))
		self.mr1.setFrameShape(QFrame.WinPanel)
		self.mr1.setFrameShadow(QFrame.Plain)
		self.mr1.setObjectName("mr1")

		self.logo = QLabel(self.mr1)
		self.logo.setGeometry(QRect(10, 10, 71, 51))
		self.logo.setFrameShape(QFrame.WinPanel)
		self.logo.setText("")
		self.logo.setPixmap(QPixmap(mg("../img/logo1.jpg")))
		self.logo.setScaledContents(True)
		self.logo.setObjectName("logo")

		self.minx = QLabel(self.mr1)
		self.minx.setGeometry(QRect(460, 20, 35, 35))
		self.minx.setMaximumSize(QSize(35, 35))
		self.minx.setCursor(QCursor(Qt.PointingHandCursor))
		self.minx.setFrameShape(QFrame.WinPanel)
		self.minx.setPixmap(QPixmap(mg("../img/min.ico")))
		self.minx.setScaledContents(True)
		self.minx.setObjectName("minx")

		self.sal = QLabel(self.mr1)
		self.sal.setGeometry(QRect(510, 20, 35, 35))
		self.sal.setMaximumSize(QSize(35, 35))
		self.sal.setCursor(QCursor(Qt.PointingHandCursor))
		self.sal.setFrameShape(QFrame.WinPanel)
		self.sal.setText("")
		self.sal.setPixmap(QPixmap(mg("../img/cierre.ico")))
		self.sal.setScaledContents(True)
		self.sal.setObjectName("sal")

		self.ms1 = QLabel(self.mr1)
		self.ms1.setGeometry(QRect(100, 10, 331, 51))
		self.ms1.setFrameShape(QFrame.NoFrame)
		self.ms1.setAlignment(Qt.AlignCenter)
		self.ms1.setObjectName("ms1")
		self.logo.raise_()
		self.minx.raise_()
		self.sal.raise_()
		self.ms1.raise_()
		self.grid2.addWidget(self.mr1, 0, 0, 1, 1)

		self.mr2 = QFrame(self.lobox)
		self.mr2.setFrameShape(QFrame.WinPanel)
		self.mr2.setFrameShadow(QFrame.Plain)
		self.mr2.setObjectName("mr2")

		self.ncr = QLabel(self.mr2)
		self.ncr.setGeometry(QRect(180, 80, 211, 41))
		self.ncr.setFrameShape(QFrame.NoFrame)
		self.ncr.setAlignment(Qt.AlignCenter)
		self.ncr.setObjectName("ncr")

		self.ncor = QLineEdit(self.mr2)
		self.ncor.setGeometry(QRect(90, 130, 411, 41))
		self.ncor.setObjectName("ncor")

		self.ncont = QLineEdit(self.mr2)
		self.ncont.setGeometry(QRect(90, 230, 411, 41))
		self.ncont.setEchoMode(QLineEdit.Password)
		self.ncont.setObjectName("ncont")

		self.cont = QLabel(self.mr2)
		self.cont.setGeometry(QRect(180, 180, 211, 41))
		self.cont.setFrameShape(QFrame.NoFrame)
		self.cont.setAlignment(Qt.AlignCenter)
		self.cont.setObjectName("cont")

		self.entrar = QPushButton(self.mr2)
		self.entrar.setGeometry(QRect(90, 280, 181, 41))
		self.entrar.setCursor(QCursor(Qt.PointingHandCursor))
		self.entrar.setObjectName("entrar")

		self.borrar = QPushButton(self.mr2)
		self.borrar.setGeometry(QRect(320, 280, 181, 41))
		self.borrar.setCursor(QCursor(Qt.PointingHandCursor))
		self.borrar.setObjectName("borrar")

		self.error = QLabel(self.mr2)
		self.error.setGeometry(QRect(20, 20, 541, 41))
		self.error.setAlignment(Qt.AlignCenter)
		self.error.setObjectName("error")
		self.grid2.addWidget(self.mr2, 2, 0, 1, 1)
		self.grid1.addWidget(self.lobox, 0, 0, 1, 1)

		self.lobox.setTitle("Sinergia !!")
		self.ms1.setText("Iniciar Sesion")
		self.ncr.setText("Nombre o Correo:")
		self.cont.setText("Contraseña:")
		self.entrar.setText("Entrar")
		self.borrar.setText("Cancelar")
		# self.error.setText("Mensajes de error")


		self.minx.mouseReleaseEvent = self.min


#esto ya no va aqui  minpero este es el grefico 


# #comenta esto
	def min(self, _):
		''' Metodo para minimizar el formulario '''
		if not self.isMinimized():
			self.showMinimized()
		else:
			self.setWindowState(Qt.WindowNoState)

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.dragPos = event.globalPos()
			event.accept()


# if __name__ == "__main__":
# 	app = QApplication(sys.argv)
# 	ap = Entrar()
# 	ap.show()
# 	sys.exit(app.exec_())

