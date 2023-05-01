from run import app 
from flask import render_template, flash, request, redirect, url_for
from forms import ResultForm
from model import ResultData


@app.route('/', methods=['GET', 'POST'])
def test():
	form = ResultForm()

	if request.method == 'POST':
		if form.validate_on_submit():
			roll_no = form.roll_no.data 
			roll_no = int(roll_no)

			data = ResultData.query.filter_by(roll_no=roll_no).first()

			if data:
				return redirect(f'/result/{data.roll_no}')
			else:
				flash('Something wrong with our server.Please try after some time')

		else:
			for x in form.errors.keys():
				for y in form.errors[x]:
					flash(y)

	return render_template('index.html', form=form)


@app.get('/result/<int:roll_no>')
def result(roll_no):
	data = ResultData.query.filter_by(roll_no=roll_no).first()
	data.marks = eval(data.marks)



	return render_template('result.html', data=data)