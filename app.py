from flask import Flask, request

from controller.CompareController import app

# app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
