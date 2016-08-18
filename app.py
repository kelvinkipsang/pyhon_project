from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/testdb'
db=SQLAlchemy(app)

@app.route('/')
def index():
    return "hello world"

if __name__ == "__main__":
    app.run()
