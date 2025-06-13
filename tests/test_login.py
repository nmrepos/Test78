import subprocess
import os
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import socket

def find_free_port():
    with socket.socket() as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def test_login():
    DB_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')
    DB_PORT = int(os.getenv('MYSQL_PORT', '3306'))
    DB_USER = os.getenv('MYSQL_USER', 'root')
    DB_PASS = os.getenv('MYSQL_PASSWORD', 'root')
    DB_NAME = os.getenv('MYSQL_DATABASE', 'testapp')

    PORT = find_free_port()
    app_proc = subprocess.Popen(['python', 'app.py'], env={**os.environ, 'FLASK_ENV': 'production', 'PORT': str(PORT)})
    time.sleep(5)

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(f'http://localhost:{PORT}/')
        driver.find_element(By.NAME, 'username').send_keys('testuser')
        driver.find_element(By.NAME, 'password').send_keys('secret')
        driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()
        time.sleep(2)
    finally:
        driver.quit()
        app_proc.terminate()
        app_proc.wait()

    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    cur = conn.cursor()
    cur.execute('SELECT username, password FROM users WHERE username=%s', ('nidhun',))
    result = cur.fetchone()
    cur.close()
    conn.close()
    assert result == ('nidhun', 'nidhun'), f"Expected ('nidhun', 'nidhun'), got {result}"

if __name__ == '__main__':
    test_login()
