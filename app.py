from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def health_check():
    return jsonify({"healthy": True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
