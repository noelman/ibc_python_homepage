from flask import Flask
import pymysql

app = Flask(__name__)
app.secret_key = "Wi8zoSxqbbVCawRcDUR0"

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "",
        db='ibc',
        )
      
    cur = conn.cursor()
    cur.execute("select * from act_franchise")
    output = cur.fetchall()
    print(output)
      
    # To close the connection
    conn.close()

@app.route('/')
def index():
    return "waddup"   

if __name__== '__main__':
    app.secret_key='Wi8zoSxqbbVCawRcDUR0'
    app.run(debug=True)    