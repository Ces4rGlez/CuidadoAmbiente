from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/importancia')
def importancia():
    return render_template('importancia.html')

@app.route('/sistema-gestion')
def sistema_gestion():
    return render_template('sistema_gestion.html')

@app.route('/futuras-generaciones')
def futuras_generaciones():
    return render_template('futuras_generaciones.html')

@app.route('/tres-r')
def tres_r():
    return render_template('tres_r.html')

if __name__ == '__main__':
    app.run(debug=True)
