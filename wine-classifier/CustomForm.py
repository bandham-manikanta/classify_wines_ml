from wtforms import validators, SubmitField, FloatField
from flask_wtf import FlaskForm

class CustomForm(FlaskForm):
    
    alcohol = FloatField("Alcohol",default=1.09715891, validators=[validators.Required(),validators.NumberRange(max=20)])
    alcalinity_of_ash = FloatField("Alcalinity of ash",default=0.03818817, validators= [validators.Required(),validators.NumberRange(max=35)])
    total_phenols = FloatField("Total phenols",default=-0.77435468, validators= [validators.Required(),validators.NumberRange(max=5)])
    flavanoids = FloatField("Flavanoids",default=-1.17340812, validators= [validators.Required(),validators.NumberRange(max=6)])
    nonflavanoid_phenols = FloatField("Non-flavanoid phenols",default=0.95086908, validators= [validators.Required(),validators.NumberRange(max=1)])
    proanthocyanins = FloatField("Proanthocyanins",default=-0.05852291, validators= [validators.Required(),validators.NumberRange(max=5)])
    color_intensity = FloatField("Color intensity",default=1.75358079, validators= [validators.Required(),validators.NumberRange(max=20)])
    od280_od315_of_diluted_wines = FloatField("OD280/OD315 of diluted wines",default=-1.37218977, validators= [validators.Required(),validators.NumberRange(max=10)])
    proline = FloatField("Proline",default=-0.87113571, validators= [validators.Required()])
    submit = SubmitField("Predict")
