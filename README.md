# Sample Login App

This repository contains a simple Flask web application with a login form that inserts user credentials into a MySQL database. A Selenium script demonstrates how to automate the login process and verify the database entry.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start a MySQL server. In a GitHub Codespace you can quickly launch one with Docker:

```bash
docker run -d --name login-mysql -p 3307:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=yes mysql:8
```

3. Create the database and table by running the helper script. The connection parameters can be customised with `MYSQL_*` environment variables (see below):

```bash
python init_db.py
```

4. Run the Flask app:

```bash
python app.py
```

5. Optionally run the Selenium test suite (requires Firefox and geckodriver):

```bash
pytest -q
```

The test will open a browser, submit the login form with a sample user, and then query the database to show the inserted row.

### Environment Variables

The application reads the following environment variables for MySQL connectivity (defaults shown):

```
MYSQL_HOST=localhost
MYSQL_PORT=3307
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=testapp
MYSQL_SOCKET=/workspace/mysqldata/mysql.sock
```

Adjust these as needed if your MySQL container is configured differently.
