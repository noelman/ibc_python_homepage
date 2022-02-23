from flask import Flask

app = Flask(__name__)
app.secret_key = "Wi8zoSxqbbVCawRcDUR0"

@app.route('/')
def index():
    return "waddup"

if __name__== '__main__':
    app.secret_key='Wi8zoSxqbbVCawRcDUR0'
    app.run(debug=True)    