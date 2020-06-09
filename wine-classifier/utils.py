import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np

def get_sample_data():
    raw_data = datasets.load_wine()
    df = pd.DataFrame(data=raw_data.data, columns=raw_data.feature_names)
    df['target'] = raw_data['target']
    df['class'] = df['target'].map(lambda ind: raw_data['target_names'][ind])
    df.drop(['class', 'hue', 'magnesium', 'ash', 'malic_acid'],
            axis='columns', inplace=True)

    # 0==>0,1
    # 1==>59,60
    # 2==>130,131

    X = df.drop('target', axis='columns')
    y = df['target']

    X = StandardScaler().fit_transform(X)
    y_ = list(y[0:2]) + list(y[59:61]) + list(y[130:132])
    X_ = np.concatenate((X[0:2], X[59:61], X[130:132]))
    target_ = {'y': y_}

    temp_df = pd.DataFrame(data=X_, index=[i for i in range(X_.shape[0])], columns=[
                           'f'+str(i) for i in range(X_.shape[1])])
    temp_df['target'] = pd.DataFrame(target_)

    temp_df.columns = ['alcohol', 'alcalinity_of_ash', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols',
                       'proanthocyanins', 'color_intensity', 'od280/od315_of_diluted_wines', 'proline', 'target']
    return temp_df
