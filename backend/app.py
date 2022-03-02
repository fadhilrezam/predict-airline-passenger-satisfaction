from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
with open("model_gboost.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/") # homepage (get)
def model_prediction():
    ct = eval(request.args.get('ct'))
    age = eval(request.args.get('age'))
    tot = eval(request.args.get('tot'))
    kelas = eval(request.args.get('kelas'))
    fd = eval(request.args.get('fd'))
    wifi = eval(request.args.get('wifi'))
    booking = eval(request.args.get('booking'))
    boarding = eval(request.args.get('boarding'))
    seat = eval(request.args.get('seat'))
    entertain = eval(request.args.get('entertain'))
    onboard = eval(request.args.get('onboard'))
    leg = eval(request.args.get('leg'))
    service = eval(request.args.get('service'))
    clean = eval(request.args.get('clean'))

    new_data = [ct, age, tot, kelas, fd, wifi, booking, boarding, seat, entertain, onboard, leg, service, clean]
    res = model.predict([new_data])
    response = {'status':'success',
            'code':200,
            'data':{'result':str(res[0])}
            }
    return jsonify(response)

@app.route("/predict", methods=['POST'])
def prediction_post():
    content = request.json
    data = [content['ct'],
            content['age'],
            content['tot'],
            content['kelas'],
            content['fd'],
            content['wifi'],
            content['booking'],
            content['boarding'],
            content['seat'],
            content['entertain'],
            content['onboard'],
            content['leg'],
            content['service'],
            content['clean'],
            ]
    res = model.predict([data])
    response = {'status':'success',
            'code':200,
            'data':{'result':str(res[0])}
            }
    return jsonify(response)

app.run(debug=True)
