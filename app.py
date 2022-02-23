from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = "Wi8zoSxqbbVCawRcDUR0"

mysql = MySQL()

# config mysql
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ibc'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    
    return "waddup"   

if __name__== '__main__':
    #mysqlconnect()
    app.secret_key='Wi8zoSxqbbVCawRcDUR0'
    app.run(debug=True)    