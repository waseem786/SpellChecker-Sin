# bottleMain.py

from bottle import route
from bottle import template, run

@route('/hi/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(host='localhost', port=8080, debug=True)

#if i type http://localhost:8080/hi/
#if i type http://localhost:8080/hello/Stranger
# out put is same : Hello Stranger, how are you?

