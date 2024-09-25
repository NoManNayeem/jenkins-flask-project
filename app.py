import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(filename='logs/flask.log', level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home page accessed")
    return "Hello, Jenkins!"

if __name__ == '__main__':
    app.run(debug=True)
