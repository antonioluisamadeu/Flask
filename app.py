from flask import Flask, render_template, request
import ds_script

app = Flask(__name__)

@app.route('/form')
def form():
	return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
	if request_method == 'POST':
		data_from_form = request.form['InputData']
		df = ds_script.generate_data(data_from_form)
		return df_to_html()

if __name__=='__main__':
	app.run(debug=True)