from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, validators, RadioField
from wtforms import widgets, SelectMultipleField


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

check_box_caracteristicas = [
    'Academia',
    'Animais permitidos',
    'Churrasqueira',
    'Condomínio fechado',
    'Elevador',
    'Piscina',
    'Playground',
    'Portaria 24h',
    'Portão eletrônico',
    'Salão de festas',
]

check_box_localizacao = [
    'Zona Central',
    'Zona Norte',
    'Zona Oeste',
    'Zona Sul'
]

class ImovelForm(FlaskForm):
    andar = IntegerField('Andar', [validators.DataRequired()])
    area_total = FloatField('Area do imóvel', [validators.DataRequired()])
    banheiros = IntegerField('Banheiros', [validators.DataRequired()])
    quartos = IntegerField('Quartos', [validators.DataRequired()])
    suites = IntegerField('Suites', [validators.InputRequired()])
    vaga = IntegerField('Vaga', [validators.InputRequired()])
    condominio = FloatField('Valor comdomínio', [validators.InputRequired()])
    iptu = FloatField('Valor IPTU', [validators.InputRequired()])

    # create a list of value/description tuples
    files = [(x, x) for x in check_box_caracteristicas]
    caracteristicas = MultiCheckboxField('Características', choices=files)
    files2 = [(x, x) for x in check_box_localizacao]
    localizacao = RadioField('Localização', choices=files2)

