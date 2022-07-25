from datetime import datetime
import re
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Plate.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Plate(db.Model):
    Sno= db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(500), nullable=False)
    Date=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.title} - {self.desc} - {self.Sno}"
@app.route('/', methods=['GET' , 'POST'])
def hello_world():
    if request.method=="POST":
        title = request.form['title']
        desc = request.form['desc']
        plate = Plate(title=title,desc=desc)
        db.session.add(plate)
        db.session.commit()
    allPlate= Plate.query.all()
    print(allPlate)
    return render_template('index.html', allPlate=allPlate)
@app.route('/show')
def products():
    allPlate = Plate.query.all()
   
    return 'This is products page'
if __name__=='__main__':
    app.run(debug=True, port=8000)   