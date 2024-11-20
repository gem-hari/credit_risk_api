from flask import Flask, request, jsonify
from core.main import calculate_risk
app = Flask(__name__)

@app.route('/calculate-risk', methods=['POST'])
def calculate_risk_endpoint():
    try:
        print("Got the request")
        data = request.get_json()
        fico_score = data.get("fico_score")
        dti = data.get("dti")
        mths = data.get("mths")

        if None in (fico_score, dti, mths):
            return jsonify({"error": "Missing one or more required fields"}), 400

        decision = calculate_risk(fico_score, dti, mths)
        return jsonify({"decision": decision})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
