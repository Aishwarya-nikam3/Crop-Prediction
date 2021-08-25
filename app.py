from flask import Flask, escape, request, render_template
from flask_cors import cross_origin
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')
model = pickle.load(open('./model/crop.pkl', 'rb'))
print('Model Loaded')

@app.route('/', methods=['GET'])
@cross_origin()
def new():
    return render_template('new.html')


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        nitro = request.form['nitro']
        phosphorous = request.form['phosphorous']
        potassium = request.form['potassium']
        temp = request.form['temp']
        humidity = request.form['humidity']
        ph = request.form['ph']
        rainfall = request.form['rainfall']

        input = [[nitro,phosphorous,potassium,temp,humidity,ph,rainfall]]
        prediction = model.predict(input)
        print(prediction)
        

        return render_template('new.html', prediction_text1 = 'You can plant- ', prediction_text2 = prediction[0])

    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)