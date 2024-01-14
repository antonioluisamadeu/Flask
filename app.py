from flask import Flask, render_template, request
import ds_script  # Import the script where 'generate_data' is defined

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data_from_form = request.form['inputData']
        df = ds_script.generate_data(data_from_form)
        return df.to_html()  # Convert DataFrame to HTML to display it

if __name__ == '__main__':
    app.run(debug=True)
