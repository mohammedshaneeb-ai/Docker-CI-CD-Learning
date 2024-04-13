from flask import Flask
import os
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"
# changes to check CI-CD

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
