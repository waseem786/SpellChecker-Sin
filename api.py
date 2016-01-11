# -*- coding: utf-8 -*-

from bottle import route, template, run


@route('/')
@route('/spellcheck/<word>', method="GET")
def spellcheck(word='NOT FOUND'):
    return template('INPUT WORD {{word}}', word=word)


run(host='localhost', port=8080, debug=True)
