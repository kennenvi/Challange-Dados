from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, validators


class MovelForm(FlaskForm):
    andar = IntegerField('Andar', [validators.DataRequired()])
    area_total = FloatField('Area do imóvel', [validators.DataRequired()])
    banheiros = IntegerField('Banheiros', [validators.DataRequired()])
    quartos = IntegerField('Quartos', [validators.DataRequired()])
    suites = IntegerField('Suites', [validators.DataRequired()])
    vaga = IntegerField('Vaga', [validators.DataRequired()])
    condominio = FloatField('Valor comdomínio', [validators.DataRequired()])
    iptu = FloatField('Valor IPTU', [validators.DataRequired()])
    

    # 'Academia',
    # 'Animais permitidos',
    # 'Churrasqueira',
    # 'Condomínio fechado',
    # 'Elevador',
    # 'Piscina',
    # 'Playground',
    # 'Portaria 24h',
    # 'Portão eletrônico',
    # 'Salão de festas',
    # 'Zona Central',
    # 'Zona Norte',
    # 'Zona Oeste',
    # 'Zona Sul'