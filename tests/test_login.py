import subprocess
import os
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    app_proc = subprocess.Popen(['python', 'app.py'], env=dict(os.environ, FLASK_ENV='production'))
    time.sleep(2)

    driver = webdriver.Firefox()
    try:
        driver.get('http://localhost:5000/')
        driver.find_element(By.NAME, 'username').send_keys('testuser')
        driver.find_element(By.NAME, 'password').send_keys('secret')
        driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()
        time.sleep(1)
    finally:
        driver.quit()
        app_proc.terminate()
        app_proc.wait()

    conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        port=int(os.getenv('MYSQL_PORT', '3307')),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', ''),
        database=os.getenv('MYSQL_DATABASE', 'testapp'),
        unix_socket=os.getenv('MYSQL_SOCKET', '/workspace/mysqldata/mysql.sock')
    )
    cur = conn.cursor()
    cur.execute('SELECT username, password FROM users WHERE username=%s', ('testuser',))
    result = cur.fetchone()
    cur.close()
    conn.close()
    assert result == ('testuser', 'secret')
