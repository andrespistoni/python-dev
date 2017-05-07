import MySQLdb as db 

# a = db.connect()
# print(a)

# ###################
dbhost = 'localhost'
dbusuario = 'root'
dbcontra = 'angy'
dbnombre = 'sinergia'

def conectar(x):
	dbdatos = [dbhost, dbusuario, dbcontra, dbnombre]
	con = db.connect(*dbdatos)
	curs = con.cursor()
	curs.execute(x)
	if x.startswith("SELECT") or x.startswith("select"):
		datos = curs.fetchall()
	else:
		con.commit()
		datos = None
	curs.close()
	con.close()
	return datos
