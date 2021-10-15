from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('index.html')


@app.route('/peliculas')
def pelicula():
    return render_template('pelicula.html')


@app.route('/busqueda')
def busqueda():
    return render_template('busqueda.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)


