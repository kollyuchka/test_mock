
import flask
import  json

from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "hello"


@app.route('/save', methods=['GET', 'POST'])
def save():
    if request.method == 'POST':

           data = request.data
           dataDict = json.loads(data)
           with open('storage', 'w') as f:
               for item in dataDict:

                   f.write(item+'='+str(dataDict[item]) +'\n')

           return dataDict
    else :
      return ("pop")



app.run(host="0.0.0.0", debug=True)