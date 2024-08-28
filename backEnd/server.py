from flask import Flask, jsonify
app = Flask(__name__)
CORS(app)

#BAse route
@app.route('/')
def home():
    return "Hello, World!"



if __name__ == "__main__":
    app.run(debug=True)