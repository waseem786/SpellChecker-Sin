# bottleMain.py

from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)

#when type /hello on address bar,
#route will call the word to defind hello.
#here Hello World is defined to Hello.
#So Hello World will print.
