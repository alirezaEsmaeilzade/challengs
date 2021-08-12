from flask import Flask, render_template, request
from m import cal

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('upload.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      cal(result["k"], result["t"], result["c"])
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
