
from flask import Flask, request, render_template_string

app = Flask(__name__)

students = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Management System</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #dbeafe, #e0e7ff);
            margin: 0;
            padding: 30px;
        }

        .container {
            max-width: 850px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }

        h1 {
            text-align: center;
            color: #1d4ed8;
        }

        p {
            text-align: center;
            color: #666;
        }

        input {
            width: 100%;
            padding: 13px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 7px;
        }

        button {
            width: 100%;
            padding: 13px;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 7px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background: #1e40af;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 25px;
        }

        th, td {
            padding: 12px;
            border: 1px solid #ddd;
            text-align: center;
        }

        th {
            background: #2563eb;
            color: white;
        }

        tr:nth-child(even) {
            background: #f1f5f9;
        }

        .delete {
            background: #dc2626;
            padding: 8px;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }

        .delete:hover {
            background: #991b1b;
        }

        .message {
            color: green;
            text-align: center;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>Student Management System</h1>
    <p>Python Flask Web Application</p>

    <h2>Add Student Details</h2>

    <form method="POST" action="/add">

        <input type="text"
               name="name"
               placeholder="Student Name"
               required>

        <input type="email"
               name="email"
               placeholder="Email Address"
               required>

        <input type="text"
               name="course"
               placeholder="Course Name"
               required>

        <button type="submit">Add Student</button>

    </form>

    <h2>Student Details</h2>

    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Course</th>
            <th>Action</th>
        </tr>

        {% for student in students %}
        <tr>
            <td>{{ loop.index }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.email }}</td>
            <td>{{ student.course }}</td>
            <td>
                <a class="delete"
                   href="/delete/{{ loop.index0 }}">
                   Delete
                </a>
            </td>
        </tr>
        {% endfor %}

    </table>

</div>

</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(HTML, students=students)


@app.route('/add', methods=['POST'])
def add_student():

    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    students.append({
        'name': name,
        'email': email,
        'course': course
    })

    return """
    <script>
        alert('Student Added Successfully!');
        window.location.href = '/';
    </script>
    """


@app.route('/delete/<int:index>')
def delete_student(index):

    if 0 <= index < len(students):
        students.pop(index)

    return """
    <script>
        alert('Student Deleted Successfully!');
        window.location.href = '/';
    </script>
    """


if __name__ == '__main__':
    app.run(debug=True)
