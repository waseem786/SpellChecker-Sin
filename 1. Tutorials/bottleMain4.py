#bottleMain.py

from bottle import route, run
from bottle import template


@route('/wiki/<pagename>')            # matches /wiki/Learning_Python
def show_wiki_page(pagename='hi'):
    return template('wiki {{pagename}}, how are you?', pagename=pagename)

@route('/<action>/<user>')            # matches /follow/defnull
def user_api(action='fight', user='waseem'):
    return template('{{action}}{{user}}, how are you?',action=action, user=user)

run(host='localhost', port=8080, debug=True)
