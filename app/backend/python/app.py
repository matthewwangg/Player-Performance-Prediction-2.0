from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.data_processing import predicts, predicts_custom

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Python Code"

@app.route('/api/predict', methods=['POST'])
def predict():

    predictions, optimized_team = predicts()

    return jsonify({"topPlayers": predictions, "optimizedTeam": optimized_team})

@app.route('/api/predict-custom', methods=['POST'])
def predict_custom():

    input_data = request.json.get('input')
    print(input_data)
    predictions, optimized_team = predicts_custom(input_data)

    return jsonify({"topPlayers": predictions, "optimizedTeam": optimized_team})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
