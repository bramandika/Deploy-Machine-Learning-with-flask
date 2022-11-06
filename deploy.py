from flask import Flask,render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model_saved.sav','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())


@app.route('/predict', methods=['POST','GET'])
def predict():
    ram = float(request.form['ram'])
    battery_power = float(request.form['battery_power'])
    px_height = float(request.form['battery_power'])
    px_width = float(request.form['battery_power'])
    result = model.predict([[ram,battery_power,px_height,px_width]])[0]
    return render_template('index.html',**locals())


if __name__ == '__main__':
    app.run(debug=True)
