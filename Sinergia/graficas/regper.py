#############################
import sys, os, re
import hashlib
import pathlib

#Imports absolutos
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from bd.base import *
# from bd.bdmysql import *
# from bd.bdfireb import *

class Personal(QWidget):
	def __init__(self, parent=None):
		super(Personal, self).__init__(parent=parent)

		self.setObjectName("marco")
		self.resize(764, 490)
		self.setMaximumSize(QSize(764, 490))
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
		self.setStyleSheet('background-color: #CBCECD; font-size: 24px; font-family: "NSimSun"; font-style: italic;')

		# font = QFont()
		# font.setFamily("NSimSun")
		# font.setPointSize(17)
		# font.setItalic(True)
		# self.setFont(font)

		self.grid = QGridLayout(self)
		self.grid.setObjectName("grid")

		self.boxt = QGroupBox()
		self.boxt.setAlignment(Qt.AlignCenter)
		self.boxt.setObjectName("boxt")

		self.grid2 = QGridLayout(self.boxt)
		self.grid2.setObjectName("grid2")

		self.caja = QFrame(self.boxt)
		self.caja.setMaximumSize(QSize(16777215, 16777215))
		self.caja.setFrameShape(QFrame.StyledPanel)
		self.caja.setFrameShadow(QFrame.Sunken)
		self.caja.setObjectName("caja")

		self.grid3 = QGridLayout(self.caja)
		self.grid3.setObjectName("grid3")

		self.nombre = QLabel(self.caja)
		self.nombre.setObjectName("nombre")
		self.grid3.addWidget(self.nombre, 0, 0, 1, 1)

		self.apellidos = QLabel(self.caja)
		self.apellidos.setObjectName("apellidos")
		self.grid3.addWidget(self.apellidos, 0, 1, 1, 1)

		self.nom = QLineEdit(self.caja)
		self.nom.setMaximumSize(QSize(16777215, 16777215))
		self.nom.setObjectName("nom")
		self.grid3.addWidget(self.nom, 1, 0, 1, 1)

		self.apell = QLineEdit(self.caja)
		self.apell.setMaximumSize(QSize(16777215, 16777215))
		self.apell.setObjectName("apell")
		self.grid3.addWidget(self.apell, 1, 1, 1, 1)

		self.grid2.addWidget(self.caja, 1, 0, 1, 1)

		self.caja2 =QFrame(self.boxt)
		self.caja2.setMaximumSize(QSize(16777215, 16777215))
		self.caja2.setFrameShape(QFrame.StyledPanel)
		self.caja2.setFrameShadow(QFrame.Sunken)
		self.caja2.setObjectName("caja2")

		self.grid4 = QGridLayout(self.caja2)
		self.grid4.setObjectName("grid4")

		self.correo = QLabel(self.caja2)
		self.correo.setObjectName("correo")
		self.grid4.addWidget(self.correo, 0, 0, 1, 1)

		self.dir = QLabel(self.caja2)
		self.dir.setObjectName("dir")
		self.grid4.addWidget(self.dir, 0, 2, 1, 1)

		self.corr = QLineEdit(self.caja2)
		self.corr.setMaximumSize(QSize(16777215, 16777215))
		self.corr.setObjectName("corr")
		self.grid4.addWidget(self.corr, 1, 0, 1, 2)

		self.dirr = QTextEdit(self.caja2)
		self.dirr.setMaximumSize(QSize(350, 111))
		self.dirr.setObjectName("dirr")
		self.grid4.addWidget(self.dirr, 1, 2, 2, 1)

		self.edad = QLabel(self.caja2)
		self.edad.setObjectName("edad")
		self.grid4.addWidget(self.edad, 2, 0, 1, 1)

		self.ed = QSpinBox(self.caja2)
		self.ed.setMaximum(150)
		self.ed.setObjectName("ed")
		self.grid4.addWidget(self.ed, 2, 1, 1, 1)

		self.grid2.addWidget(self.caja2, 2, 0, 1, 1)

		self.caja3 = QFrame(self.boxt)
		self.caja3.setFrameShape(QFrame.StyledPanel)
		self.caja3.setFrameShadow(QFrame.Sunken)
		self.caja3.setObjectName("caja3")
		self.grid5 = QGridLayout(self.caja3)

		self.grid5.setObjectName("grid5")

		self.telef = QLabel(self.caja3)
		self.telef.setObjectName("telef")
		self.grid5.addWidget(self.telef, 0, 0, 1, 1)

		self.caja4 = QFrame(self.caja3)
		self.caja4.setFrameShape(QFrame.StyledPanel)
		self.caja4.setFrameShadow(QFrame.Sunken)
		self.caja4.setObjectName("caja4")
		self.grid6 = QGridLayout(self.caja4)

		self.grid6.setContentsMargins(-1, 9, -1, 9)
		self.grid6.setObjectName("grid6")

		self.admin = QCheckBox(self.caja4)
		self.admin.setCursor(QCursor(Qt.PointingHandCursor))
		self.admin.setObjectName("admin")
		self.grid6.addWidget(self.admin, 1, 0, 1, 1)
		self.admin.clicked.connect(self.b1)

		self.empl = QCheckBox(self.caja4)
		self.empl.setChecked(True)
		self.empl.setCursor(QCursor(Qt.PointingHandCursor))
		self.empl.setObjectName("empl")
		self.grid6.addWidget(self.empl, 1, 1, 1, 1)
		self.empl.clicked.connect(self.b2)

		self.foto = QPushButton(self.caja4)
		self.foto.setFlat(True)
		self.foto.setCursor(QCursor(Qt.PointingHandCursor))
		self.foto.setObjectName("foto")
		self.grid6.addWidget(self.foto, 0, 0, 1, 2)

		self.grid5.addWidget(self.caja4, 0, 1, 4, 2)

		self.tel = QLineEdit(self.caja3)
		self.tel.setMaximumSize(QSize(335, 16777215))
		self.tel.setObjectName("tel")
		self.grid5.addWidget(self.tel, 1, 0, 1, 1)

		self.cont = QLabel(self.caja3)
		self.cont.setObjectName("cont")
		self.grid5.addWidget(self.cont, 2, 0, 1, 1)

		self.con = QLineEdit(self.caja3)
		self.con.setMaximumSize(QSize(335, 16777215))
		self.con.setEchoMode(QLineEdit.Password)
		self.con.setObjectName("con")
		self.grid5.addWidget(self.con, 3, 0, 1, 1)

		self.refer = QPushButton(self.caja3)
		self.refer.setFlat(True)
		self.refer.setCursor(QCursor(Qt.PointingHandCursor))
		self.refer.setObjectName("refer")
		self.grid5.addWidget(self.refer, 4, 0, 1, 1)

		self.reg = QPushButton(self.caja3)
		self.reg.setFlat(True)
		self.reg.setMaximumSize(QSize(16777215, 16777215))
		self.reg.setCursor(QCursor(Qt.PointingHandCursor))
		self.reg.setObjectName("reg")
		self.grid5.addWidget(self.reg, 4, 1, 1, 1)

		self.sal = QPushButton(self.caja3)
		self.sal.setFlat(True)
		self.sal.setCursor(QCursor(Qt.PointingHandCursor))
		self.sal.setObjectName("sal")
		self.grid5.addWidget(self.sal, 4, 2, 1, 1)

		self.grid2.addWidget(self.caja3, 3, 0, 1, 1)

		self.mens = QLabel(self.boxt)
		self.mens.setAlignment(Qt.AlignCenter)
		self.mens.setObjectName("mens")
		self.grid2.addWidget(self.mens, 0, 0, 1, 1)
		self.grid.addWidget(self.boxt, 0, 1, 1, 1)

		self.setTabOrder(self.nom, self.apell)
		self.setTabOrder(self.apell, self.corr)
		self.setTabOrder(self.corr, self.dirr)
		self.setTabOrder(self.dirr, self.ed)
		self.setTabOrder(self.ed, self.tel)
		self.setTabOrder(self.tel, self.foto)
		self.setTabOrder(self.foto, self.con)
		self.setTabOrder(self.con, self.admin)
		self.setTabOrder(self.admin, self.empl)
		self.setTabOrder(self.empl, self.refer)
		self.setTabOrder(self.refer, self.reg)
		self.setTabOrder(self.reg, self.sal)

		self.boxt.setTitle(("Registro del personal"))
		self.nombre.setText(("Nombres:"))
		self.apellidos.setText(("Apellidos:"))
		self.correo.setText(("Correo:"))
		self.dir.setText(("Direccion:"))
		self.edad.setText(("Edad:"))
		self.telef.setText(("Telefono:"))
		self.admin.setText(("Admin"))
		self.empl.setText(("Empleado"))
		self.foto.setText(("Subir foto !!"))
		self.cont.setText(("Contraseña:"))
		self.refer.setText(("Referencias !!!"))
		self.reg.setText(("Registrar"))
		self.sal.setText(("Salir"))
# #########################################

		self.nom.textChanged.connect(self.valnom)
		self.apell.textChanged.connect(self.valape)
		self.corr.textChanged.connect(self.valcor)
		self.dirr.textChanged.connect(self.valdir)
		self.ed.valueChanged.connect(self.valed)
		self.tel.textChanged.connect(self.valtel)
		self.con.textChanged.connect(self.valcon)
		self.admin.stateChanged.connect(self.valper)

		self.sal.clicked.connect(self.x)
		self.foto.clicked.connect(self.subirfoto)
		self.reg.clicked.connect(self.valformu)
		
########################################
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.dragPos = event.globalPos()
			event.accept()
#########################################
	def x(self, _):
		self.close()
########################################
	def subirfoto(self):
		ruta = 'fotos'
		fichero = QFileDialog.getOpenFileName(self, "Subir archivo",
                QDir.currentPath())
		destino = os.path.split(fichero[0])[-1] 

		if fichero[0]=="":
			self.mens.setText("No has selecionado nada :( ")
		else:
			print(fichero[0])
			pix = QPixmap(fichero[0])
			img = QImage(fichero[0])

			# self.mg.setPixmap(pix)
			# self.mg.setScaledContents(True)
			# self.mens.setText("Imagen subida exitosamente")

			folder = os.path.join(os.getcwd(), ruta)
			
			if not os.path.exists(folder):
				os.makedirs(folder)  
		
			directorio = os.path.join(folder, destino)
			response = img.save(directorio)
			if response:
				self.mens.setText("Imagen subida exitosamente")
			else:
				self.mens.setText("Solo imagenes")
#########################################
			# check1.stateChanged[bool].connect(lambda x: check2.setChecked(not x))
#################################
	def b1(self):
		ad = self.admin.isChecked()
		empl = self.empl.isChecked()
		if ad == True:
			self.empl.setChecked(False)
#################################
	def b2(self):
		ad = self.admin.isChecked()
		empl = self.admin.isChecked()
		if empl == True:
			self.admin.setChecked(False)
# ######################################

	def valnom(self):
		nr = self.nom.text()
		nrr = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]{3,20}$', nr, re.I)
		if len(nr.strip()) == 0:
			self.mens.setText("Nombre vacio ##")
			return False
		elif not nrr:
			self.mens.setText("Solo letras, min 3, max 20")
			return False
		else:
			return True

	def valape(self):
		al = self.apell.text()
		ape = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]{3,20}$', al, re.I)
		if len(al.strip()) == 0:
			self.mens.setText("Apellidos vacios ##")
			return False
		elif not ape:
			self.mens.setText("Solo letras, min 3, max 20")
			return False
		else:
			return True

	def valcor(self):
		cr = self.corr.text()
		# '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$'
		crr = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$', cr, re.I)
		if len(cr.strip()) == 0:
			self.mens.setText("Correo vacio ##")
			return False
		elif not crr:
			self.mens.setText("Formato valido para correo, [y que sea unico] !")
			return False
		else:

			return True

	def valdir(self):
		dr = self.dirr.toPlainText()
		# '[a-zA-Z1-9À-ÖØ-öø-ÿ]+\.?(( |\-)[a-zA-Z1-9À-ÖØ-öø-ÿ]+\.?)* (((#|[nN][oO]\.?) ?)?\d{1,4}(( ?[a-zA-Z0-9\-]+)+)?)'
		dirr = re.match('^[a-z-0-9\sáéíóúàèìòùäëïöüñ]{10,150}$', dr, re.I)
		if len(dr.strip()) == 0:
			self.mens.setText("Dirección vacia ##")
			return False
		elif not dirr:
			self.mens.setText("Letras, numeros, min 10, max 150")
			return False
		else:
			return True

	def valed(self):
		edd = self.ed.value()
		if edd == 0:
			self.mens.setText("Edad vacia ##")
			return False
		elif edd < 18:
			self.mens.setText("Tiene que ser mayor de edad")
			return False
		else:
			return True

	def valtel(self):
		tf = self.tel.text()
		tell = re.match('0{0,2}([\+]?[\d]{1,3} ?)?([\(]([\d]{2,3})[)] ?)?[0-9][0-9 \-]{7,}( ?([xX]|([eE]xt[\.]?)) ?([\d]{1,5}))?', tf, re.I)
		if len(tf.strip()) == 0:
			self.mens.setText("Telefono vaci0 ##")
			return False
		elif not tell:
			self.mens.setText("Solo formato de telefono valido, min 8")
			return False
		else:
			return True

	def valcon(self):
		cn = self.con.text()
		cnn = re.match('^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ0-9!@#\$%\^&\*\?_~\/]{5,20}$', cn, re.I)
		if len(cn.strip()) == 0:
			self.mens.setText("Contraseña vacia ##")
			return False
		elif not cnn:
			self.mens.setText("Min 5, minusculas y cualquier caracter")
			return False
		else:
			return True

	def valper(self):
		if  self.admin.isChecked():
			self.rol = 1
			self.mens.setText("Rol: Administrador")
			#print(rol)
		else:
			self.rol = 2
			self.mens.setText("Rol: Empleado")

	def lim(self):
		self.nom.setText('')
		self.apell.setText('')
		self.corr.setText('')
		self.dirr.setText('')
		self.ed.value()
		self.tel.setText('')
		self.con.setText('')
		self.nom.setFocus()		
# ###########################################
	def valformu(self):
		# n = self.valnom()
		# a = self.valape()
		# c = self.valcor()
		# d = self.valdir()
		# e = self.valed()
		# t = self.valtel()
		# p = self.valcon()
		# r = self.valper()
		# if n and a and c and d and e and t and p:
		nr = self.nom.text()
		al = self.apell.text()    
		cr = self.corr.text()     
		dr =  self.dirr.toPlainText()  
		edd = self.ed.value()
		tf = self.tel.text()
		ft = self.foto.isCheckable()
		cn =  self.con.text()  
		px = hashlib.sha1(cn.encode('utf-8'))
		px = px.hexdigest()
		rf = self.refer.isCheckable()

		# sql = ("insert into usuarios (nombre, apellidos, correo, domicilio, edad, tel, foto, contra, rol, idrefer) values('{0}', '{1}' , '{2}', '{3}', {4} ,'{5}' ,'{6}' ,'{7}', {8}, {9} )").format(nr, al, cr, dr, edd, tf, ft,px, self.rol, rf)

		# sql = ("insert into personal (nombre, apellidos, correo, domi, edad, tel, foto, con, rol, idrefer) values('{0}', '{1}' , '{2}', '{3}', {4} ,'{5}' ,null ,'{7}', {8}, null )").format(nr, al, cr, dr, edd, tf, ft,px, self.rol, rf)
		sql = ("insert into personal (nombre, apellidos, correo, domi, edad, tel, foto, con, idrefer) values('{0}', '{1}' , '{2}', '{3}', {4} ,'{5}' ,null ,'{7}', null )").format(nr, al, cr, dr, edd, tf, ft,px, rf)
		self.datos = conectar(sql)
		# print(sql)
		self.mens.setText("Registro exitoso")
		self.lim()
	# else:
		self.mens.setText("Fallo el registro, falta algun dato")
			
# #########################################
if __name__ == "__main__":
	app = QApplication(sys.argv)
	ap = Personal()
	ap.show()
	sys.exit(app.exec_())