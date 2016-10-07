from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'thisisnotsecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def turtles():
    return redirect('/ninjas/turtle')

@app.route('/ninjas/')
def turtles2():
    return redirect('/ninjas/turtle')

@app.route('/ninjas/<ninjatype>')
def ninjas(ninjatype):
    if (len(ninjatype) < 1):
        ninjatype = 'turtle'
    if (ninjatype != 'blue' and ninjatype != 'orange' and ninjatype != 'red' and ninjatype != 'purple' and ninjatype != 'turtle'):
        ninjatype = 'april'
    return render_template('ninjas.html', ninjatype = ninjatype)

app.run(debug = True)
