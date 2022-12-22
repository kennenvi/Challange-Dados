from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', titulo='Montando imóvel')



if __name__ == '__main__':
    app.run()