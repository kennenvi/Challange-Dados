from flask import Flask, render_template, url_for
from helpers.formClasses import MovelForm


SECRET_KEY = 'development'
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/movel',methods=['post','get'])
def movel():
    form = MovelForm()
    if form.validate_on_submit():
        print(form.caracteristicas.data)
        return render_template("success.html", data=form.caracteristicas.data)
    else:
        print("Validation Failed")
        print(form.errors)
    return render_template('example.html',form=form)


# @app.route('/')
# def index():
#     return render_template('index.html', titulo='Montando imóvel')



if __name__ == '__main__':
    app.run()