# bottleMain.py

from bottle import route
from bottle import template, run
from bottle import static_file



@route('/images/<filename:re:.*\.PNG>')
def send_image(filename):
    return static_file(filename, root='/C:/Users/Waseem/Desktop/Bottle Tutorials/1. Tutorials', mimetype='image/PNG')

@route('/static/<filename:path>')
def send_static(filename='bottleMain.PNG'):
    return static_file(filename, root='/C:/Users/Waseem/Desktop/Bottle Tutorials/1. Tutorials')




run(host='localhost', port=8080, debug=True)
