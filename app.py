from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submit_data', methods=['GET', 'POST'])
def submit_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        student_id = request.form['student_id']
        grades = request.form.getlist('question0')
        satisfaction = request.form['question1']
        suggestions = request.form['suggestions']

        with open('submitted_data.txt', 'a') as file:
            file.write(f'Name: {name}\n')
            file.write(f'Email: {email}\n')
            file.write(f'Student ID: {student_id}\n')
            for grade in grades:
                file.write(f'Grade: {grade}\n')
            file.write(f'Overall Satisfaction: {satisfaction}\n')
            file.write(f'Suggestions: {suggestions}\n\n')

        return redirect(url_for('success'))

if __name__ == '__main__':
    app.run(debug=True)
