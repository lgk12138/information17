# This is my first flask object.

from flask import Flask

app=Flask(__name__)

@app.route('/')
def helloworld():
    return 'Hello World! Im Barca!'

if __name__ = '__main__'
    app.run(debug=True)
