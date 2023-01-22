from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return "main"

@app.route('/id/<int:id>', methods=['GET'])
def get(id):
    if id>=5000:
        return {"result":True}
    else:
        return {"result":False}

@app.route('/id', methods=['POST'])
def post():
    jsonFile = request.get_json()

    _name = jsonFile["name"]

    return {"name": _name}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)