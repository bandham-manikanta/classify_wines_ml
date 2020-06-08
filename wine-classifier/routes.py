from flask import jsonify, make_response, request, abort, render_template
from flask import current_app as app
import pickle as pkl
import numpy as np
from CustomForm import CustomForm

model = pkl.load(open('wine_clssifier.pkl', 'rb'))


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
    pred_result = model.predict(data)
    print("************",pred_result)
    return render_template('result.html', result=pred_result[0])
