from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('response.html',context="you are in homepage")

@app.route('/view',methods=['GET'])
def view():
    return render_template('response.html',context="you are in viewpage")

@app.route("/add",methods=['GET'])
def addition_form():
    return render_template('form.html',path="/addition_form")

@app.route("/addition_form",methods=['POST'])
def addition():
    num1=request.form['a_val']
    num2=request.form['b_val']
    return render_template('response.html',context=f'{int (num1)+int(num2)}')

@app.route("/sub",methods=['GET'])
def subtraction_form():
    return render_template('form.html',path="/subtraction_form")

@app.route("/subtraction_form",methods=['POST'])
def subtraction():
    num1=request.form['a_val']
    num2=request.form['b_val']
    return render_template('response.html',context=f'{int (num1)-int(num2)}')

@app.route("/mul",methods=['GET'])
def multiplication_form():
    return render_template('form.html',path="/multiplication_form")

@app.route("/multiplication_form",methods=['POST'])
def multiplication():
    num1=request.form['a_val']
    num2=request.form['b_val']
    return render_template('response.html',context=f'{int (num1)*int(num2)}')

@app.route('/div',methods=['GET'])
def division_form():
    return render_template("form.html",path="/shareef")

@app.route('/shareef',methods=['post'])
def division():
    num1=request.form['a_val']
    num2=request.form['b_val']
    return render_template('response.html',context=f'{int(num1)/int(num2)}')

app.run()
