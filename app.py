#app.py
from flask import Flask

app = Flask(__name__)

#app route
@app.route('/')
def index():
    return 'Hello World'

#say hello! 
#create a form through jinja and then get the input and return hello
@app.route('/hello')
def hello():
    name = input('what\'s your name ?\n')
    message = ('Hello ', name)
    return message
    

#specify host and port
app.run(debug=True, host='0.0.0.0', port=8000)