import requests

def send_risk_request(fico_score, dti, mths):
    url = "http://127.0.0.1:5000/calculate-risk/"
    
    payload = {
        "fico_score": fico_score,
        "dti": dti,
        "mths": mths
    }
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed with status code {response.status_code}", "details": response.text}
    
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":   
    fico_score = 480
    dti = 24
    mths = 0 
    result = send_risk_request(fico_score, dti, mths)
    print(result)
