import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By

# start the flask app in a subprocess
import subprocess, os

app_proc = subprocess.Popen(['python', 'app.py'], env=dict(os.environ, FLASK_ENV='production'))

time.sleep(2)  # give server time to start

try:
    driver = webdriver.Firefox()
    driver.get('http://localhost:5000/')
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('secret')
    driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()
    time.sleep(1)
finally:
    driver.quit()
    app_proc.terminate()
    app_proc.wait()

# check database for inserted user
conn = mysql.connector.connect(host='localhost', port=3307, user='root', password='', database='testapp', unix_socket='/workspace/mysqldata/mysql.sock')
cur = conn.cursor()
cur.execute("SELECT username, password FROM users WHERE username=%s", ('testuser',))
result = cur.fetchone()
print(result)
cur.close()
conn.close()
