from flask import Flask
from default.engine import create_all_tables_database

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    create_all_tables_database()
    app.run()
