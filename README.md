# Sample Login App

This repository contains a simple Flask web application with a login form that inserts user credentials into a MySQL database. A Selenium script demonstrates how to automate the login process and verify the database entry.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start a MySQL server. The included example expects a server running locally on port `3307` with a root user and no password. You can start a temporary server with:

```bash
mysqld --initialize-insecure --datadir=/workspace/mysqldata
mysqld --datadir=/workspace/mysqldata --socket=/workspace/mysqldata/mysql.sock --port=3307 --skip-networking=0 &
```

3. Create the database and table:

```bash
mysql --socket=/workspace/mysqldata/mysql.sock -u root -e "CREATE DATABASE testapp; USE testapp; CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255));"
```

4. Run the Flask app:

```bash
python app.py
```

5. Optionally run the Selenium test (requires Firefox and geckodriver):

```bash
python test_login.py
```

The test will open a browser, submit the login form with a sample user, and then query the database to show the inserted row.
