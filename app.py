from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/testdb'
db=SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), unique=True)
    sname = db.Column(db.String(20), unique=True)

    def __init__(self, fname, sname):
        self.fname = fname
        self.sname = sname

    def __repr__(self):
        return '<User %r>' % (self.nickname)



@app.route('/')
def index():
    return "hello world"

if __name__ == "__main__":
    app.run()
