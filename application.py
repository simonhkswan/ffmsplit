from flask import Flask

application = api = Flask(__name__)

@api.route("/")
def hello():
    return "If you can see this. Its working!"

if __name__ == "__main__":
    api.run()