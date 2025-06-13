from flask import Flask, request, render_template_string, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='',
        database='testapp',
        unix_socket='/workspace/mysqldata/mysql.sock'
    )

HTML_FORM = '''
<!doctype html>
<title>Login</title>
<h1>Login Form</h1>
<form method="post">
  Username: <input type="text" name="username"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit" value="Login">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/success')
    return render_template_string(HTML_FORM)

@app.route('/success')
def success():
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
