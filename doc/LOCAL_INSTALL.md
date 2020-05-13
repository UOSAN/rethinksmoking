# Local installation
## Install prerequisites of rethinksmoking application

### Install MySQL Server

[Download MySQL](https://dev.mysql.com/downloads/mysql/), and install it.

During installation, when asked to "Configure MySQL Server", choose "Use Legacy Password Encryption". During installation, creating a password for the "root" user is required. Choose a password.

Add the path to mysql:
```
export PATH=$PATH:/usr/local/mysql/bin/
```

Connect to the database via
```
mysql -u root -p
```
And enter password when asked.

Create the rethinksmoking database:
```
mysql> create database rethinksmoking;
Query OK, 1 row affected (0.00 sec)
```

Create a database user named 'rethinksmoking' for the application:
```
mysql> create user 'rethinksmoking'@'localhost';
Query OK, 0 rows affected (0.01 sec)
```

Grant that user all permissions on the 'rethinksmoking' database:
```
mysql> grant all on rethinksmoking.* to 'rethinksmoking'@'localhost';
Query OK, 0 rows affected (0.00 sec)
```

Make sure the new privileges are applied:
```
mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
```

## Configuration
`rethinksmoking` is built on [Flask](https://flask.palletsprojects.com/en/1.1.x/),
and requires some configuration to run locally.
The following environment variables must be specified to configure the database connection:
```
DB_CONNECTION=mysql+pymysql
DB_HOST=127.0.0.1
DB_DATABASE=rethinksmoking
DB_USERNAME=rethinksmoking
DB_PASSWORD=<password for rethinksmoking user>
```

and the following environment variables must be specified to configure how Flask
starts the app and in what environment:
```
FLASK_APP=rethinksmoking/flask_app
FLASK_ENV=development
```

Do not use these settings in a production deployment.

To run the app in the PyCharm IDE / debugger, the `Script path:` should point to
the flask executable: `/usr/local/bin/flask`, and `Parameters:` should be `run`.
