from flask import Flask, render_template, request, redirect, url_for
from models import StudentTracker

app = Flask(__name__)
tracker = StudentTracker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_number = request.form['roll_number']
        tracker.add_student(name, roll_number)
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/add_grades/<roll_number>', methods=['GET', 'POST'])
def add_grades(roll_number):
    student = tracker.get_student(roll_number)
    if request.method == 'POST':
        grades = {
            'Math': int(request.form['math']),
            'Science': int(request.form['science']),
            'English': int(request.form['english'])
        }
        tracker.add_grades(roll_number, grades)
        return redirect(url_for('view_student', roll_number=roll_number))
    return render_template('add_grades.html', student=student)

@app.route('/view_student/<roll_number>')
def view_student(roll_number):
    student = tracker.get_student(roll_number)
    return render_template('view_student.html', student=student)

@app.route('/average_grade/<roll_number>')
def average_grade(roll_number):
    student = tracker.get_student(roll_number)
    average = tracker.calculate_average(roll_number)
    return render_template('average_grade.html', student=student, average=average)

if __name__ == '__main__':
    app.run(debug=True)
