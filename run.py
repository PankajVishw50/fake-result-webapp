from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sql'
app.config['SECRET_KEY'] = 'hard to guess'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


from views import * 

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")