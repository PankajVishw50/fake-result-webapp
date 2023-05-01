from run import db 


class ResultData(db.Model):
	__tablename__ = 'resultdata'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, nullable=False)
	roll_no = db.Column(db.Integer, nullable=False, unique=True)
	father_name = db.Column(db.Integer, nullable=False)
	marks = db.Column(db.Text)

