#bottleMain.py

from bottle import route, abort, run

@route('/restricted')
def restricted():
    abort(401, "Sorry, you can't access to that. Its mine")

#went tried to access restricted it wil show a message for 401

from bottle import redirect
@route('/wrong/url')
def wrong():
    redirect("/right/url")

#when type /wrong/url in address bar it will redirect to /right/url

run(host='localhost', port=8080, debug=True)



