from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! This is QuakeWatch!"

if __name__ == "__main__":
    # Run app on port 5001
    app.run(host="0.0.0.0", port=5001)

