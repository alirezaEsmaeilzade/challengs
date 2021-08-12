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
      plot = cal(result["a1"], result["b1"], result["c1"], result["d1"], result["a2"], result["b2"], result["c2"], result["d2"])
      return render_template("result.html",plot = plot)

if __name__ == '__main__':
   app.run(debug = True)
