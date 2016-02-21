# -*- coding: utf-8 -*-

from bottle import route, template, get, run

import bottle
import xmltodict
import sys
import os
import codecs
import libxml2
from spellchecker import Spellchecker_si

def check(user, passwd):
    if user == 'ben':
        return True
    return False

def check(user, passwd):
    if passwd == 'xyz':
        return True
    return False

@route('/spellcheck/<word>')
@bottle.auth_basic(check)
def spellcheck(word):
    
    print 'auth', bottle.request.auth
    print 'remote_addr', bottle.request.remote_addr
    
    word = word.decode('utf-8')
    if word:
        xml_output = Spellchecker_si().spellcheck(word, format='JSON')
    else:
        xml_output = "<spellcheck-result> <error> NO INPUT OR INVALID WORD </error> </spellcheck-result>"
    #json_output = xmltodict.parse(xml_output)

    return xml_output




run(host='localhost', port=8080, debug=True)
