from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hej! Din Flask-app virker.'

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/hello/<navn>')
def hello_name(navn):
    return f'Hej {navn}! Velkommen til min Flask-app.'
