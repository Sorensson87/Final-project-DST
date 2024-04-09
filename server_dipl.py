from flask import Flask, request, jsonify
import pickle
import numpy as np

# загружаем модель из файла
with open('final_pipeline.pkl', 'rb') as pkl_file: 
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def get_predict():
    data = request.json
    cols = ['status', 'baths', 'fireplace', 'city', 'sqft', 'state', 'stories', 'pool', 'property_type', 'school_rating', 'mean_distance_to_school', 'year_built', 'heating', 'cooling', 'parking', 'lotsize', 'price/sqft']
    req_f = pd.DataFrame([data], columns=cols)
    print(req_f)
    print(loaded_pipe.predict(req_f))
    pred = loaded_pipe.predict(req_f)
    return {'prediction': pred[0]}

if __name__ == '__main__':
    app.run('localhost', 5000)