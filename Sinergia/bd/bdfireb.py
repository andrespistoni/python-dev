# -*- coding: utf-8 -*-

import os, sys
import fdb as sg

#metodo de conexion
def conectar(x):
	ruta = 'sinergia.fdb'
	ruta = os.path.dirname(os.path.realpath(__file__))+"/" + ruta
	con = sg.connect(
		dsn = ruta,
		user = 'sysdba',
		password = 'angygarro',
		charset ='utf8'	
	)
	cx = con.cursor()
	cx.execute(x)
	if x.startswith("SELECT") or x.startswith("select"):
		datos = cx.fetchall()
	else:
		con.commit()
		datos = None
	cx.close()
	con.close()
	return datos
#.........................................................................................................
