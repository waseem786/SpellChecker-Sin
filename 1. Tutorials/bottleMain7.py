# bottleMain.py

from bottle import route
from bottle import static_file, run
from bottle import error


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='C:/Users/Waseem/Desktop/Bottle Tutorials/1. Tutorials/bottleMain.py')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='C:/Users/Waseem/Desktop/Bottle Tutorials/1. Tutorials/bottleMain.py')


@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='localhost', port=8080, debug=True)

