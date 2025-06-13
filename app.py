from flask import Flask, request, render_template_string, redirect
import os
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    """Create a MySQL connection using environment variables if provided."""
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        port=int(os.getenv('MYSQL_PORT', '3307')),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', ''),
        database=os.getenv('MYSQL_DATABASE', 'testapp'),
        unix_socket=os.getenv('MYSQL_SOCKET', '/workspace/mysqldata/mysql.sock'),
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
