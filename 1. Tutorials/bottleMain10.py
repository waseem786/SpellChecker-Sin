#bottleMain.py

from bottle import route, request, response, run

@route('/hello')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

run(host='localhost', port = 8080, debug = True)
