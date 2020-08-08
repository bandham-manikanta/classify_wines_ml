from flask import jsonify, make_response, request, abort, render_template
from flask import current_app as app
import pickle as pkl
import numpy as np
from CustomForm import CustomForm
import pandas as pd
from utils import get_sample_data

model = pkl.load(open('wine_clssifier.pkl', 'rb'))
temp_df = get_sample_data()


@app.route('/', methods=['GET'])
def main_page():
    form = CustomForm()
    return render_template('index.html', form=form)


@app.route('/predict', methods=['POST'])
def classify_wine():
    form = request.form
    input_data = {
        'alcohol': form['alcohol'],
        'alcalinity_of_ash': form['alcalinity_of_ash'],
        'total_phenols': form['total_phenols'],
        'flavanoids': form['flavanoids'],
        'nonflavanoid_phenols': form['nonflavanoid_phenols'],
        'proanthocyanins': form['proanthocyanins'],
        'color_intensity': form['color_intensity'],
        'od280/od315_of_diluted_wines': form['od280_od315_of_diluted_wines'],
        'proline': form['proline']
    }
    data = np.asarray([list(input_data.values())])
    result = model.predict(data)[0]
    return jsonify({'result': str(result)})


@app.route('/data', methods=['GET'])
def data_page():
    # return render_template('result.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
    # return temp_df.to_html(header="true", table_id="table")
    return render_template("data.html", data=temp_df.to_html().replace('<table border="1" class="dataframe">', '<table border="1" class="table-sm table-striped table-responsive">'))
