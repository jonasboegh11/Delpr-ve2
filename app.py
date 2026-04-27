from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hej! Din Flask-app virker.'

if __name__ == '__main__':
    app.run(debug=True)
