#from crypt import methods
#from cgitb import text
from flask import Flask , render_template, url_for , request ,session ,redirect
import dbOps as db

db.initialise_data_base('PESUfitness')

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("sample.html")


@app.route('/',methods = ['POST'])
def my_form_post():
    SRN =request.form['SRN']
    Squat_Number= db.fetch_only_count(SRN)
    Final_count = "Total number of squats you have performed is : "+Squat_Number
    return Final_count

if (__name__ == "__main__"):
    app.run(debug=True)
