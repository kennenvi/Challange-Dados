from flask import Flask, render_template, url_for, flash
from helpers.formClasses import ImovelForm
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, FloatType, StringType, ArrayType, StructField, StructType


SECRET_KEY = 'development'
app = Flask(__name__)
app.config.from_object(__name__)

spark = SparkSession.builder \
    .master('local[*]') \
    .appName("Iniciando com Spark") \
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
        flash('Preencha todos os campos obrigatórios')
        return render_template('imovel.html', form=form, titulo='Imóvel')
    
    
    types_df = [IntegerType(), FloatType(), IntegerType(), 
                IntegerType(), IntegerType(), IntegerType(), FloatType(),
                FloatType(), ArrayType(StringType(), True), StringType()]
    headers = ['andar', 'area_total', 'banheiros',
                'quartos', 'suites', 'vaga', 'condominio',
                'iptu', 'caracteristicas', 'localizacao']
    schema = StructType(
            [StructField(header, type_df, True) for header, type_df in zip(headers, types_df)]
        )
    
    dados = [(form.andar.data, form.area_total.data, form.banheiros.data,
                form.quartos.data, form.suites.data, form.vaga.data, form.condominio.data,
                form.iptu.data, form.caracteristicas.data, form.localizacao.data)]

    df = spark.createDataFrame(dados, schema)
    print(df)
    return "<h1> Sucesso </h1>"

@app.route('/')
def index():
    return render_template('index.html', titulo='Montando imóvel')


if __name__ == '__main__':
    app.run()