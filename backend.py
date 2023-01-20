# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "hello world!"

# app.run()




# class Video():
#     def __init__(self):
#         id: str
#         # frames: Frame[]
#         jsonMetaData: str


# class Frame():
#     bytes: byte



#!/usr/bin/env python
from flask import Flask, render_template, Response
from camera import Camera

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return "welcome to the app (go to /video)"

@app.route('/video')
def video():    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)