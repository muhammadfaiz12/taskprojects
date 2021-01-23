from flaskext.mysql import MySQL

def init_db(app):
   app.config['MYSQL_DATABASE_HOST'] = 'localhost'
   app.config['MYSQL_DATABASE_USER'] = 'root'
   app.config['MYSQL_DATABASE_PASSWORD'] = ''
   app.config['MYSQL_DATABASE_DB'] = 'taskproject'
   mysql = MySQL(app)
   return mysql