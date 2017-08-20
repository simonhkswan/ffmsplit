from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "If you can see this. Its working!"

if __name__ == "__main__":
    app.run()