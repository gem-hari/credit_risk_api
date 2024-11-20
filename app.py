from flask import Flask, request, jsonify
from core.main import calculate_risk
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return {"message": "API is working!"}


@app.route('/calculate-risk/', methods=['POST'])
def calculate_risk_endpoint():
    try:
        data = request.get_json()
        app.logger.info("Request received")
        app.logger.info(f"Payload: {data}")

        fico_score = data.get("fico_score",None)
        dti = data.get("dti",None)
        mths = data.get("mths",0)

        if None in (fico_score, dti, mths):
            return jsonify({"error": "Missing one or more required fields"}), 400
        if fico_score>=850 or fico_score<0:
            return jsonify({"error": "Fico score should lie between 0 and 850"}), 400
        if mths<0:
            return jsonify({"error": "Months since most recent installment account cannot be negative"}), 400

        decision = calculate_risk(fico_score, dti, mths)
        return jsonify({"decision": decision})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)