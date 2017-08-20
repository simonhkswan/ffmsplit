from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "If you can see this. Its working!"

if __name__ == "__main__":
    application.run()