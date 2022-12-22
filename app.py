from flask import Flask, render_template, url_for
from helpers.formClasses import ImovelForm
from pyspark.sql import SparkSession


SECRET_KEY = 'development'
app = Flask(__name__)
app.config.from_object(__name__)

spark = SparkSession.builder \
    .master('local[*]') \
    .appName("Iniciando com Spark") \
    .config('spark.ui.port', '4050') \
    .getOrCreate()

@app.route('/imovel')
def imovel():
    form = ImovelForm()
    return render_template('imovel.html', form=form, titulo='Imóvel')
    

@app.post('/prever')
def prever():
    form = ImovelForm()
    if not form.validate_on_submit():
        print("Validation Failed")
        print(form.errors)
        return render_template('imovel.html', form=form, titulo='Imóvel')
    
    dados = [form.andar.data, form.area_total.data, form.banheiros.data,
                form.quartos.data, form.suites.data, form.condominio.data,
                form.iptu.data, form.caracteristicas.data, form.localizacao.data]
    headers = ['andar', 'area_total', 'area_util',
                'banheiros', 'quartos', 'suites',
                'vaga', 'condominio', 'iptu',
                'caracteristicas', 'localizacao']
    df = spark.createDataFrame(dados, headers)
    print(df)

@app.route('/')
def index():
    return render_template('index.html', titulo='Montando imóvel')


if __name__ == '__main__':
    app.run()