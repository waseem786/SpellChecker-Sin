# -*- coding: utf-8 -*-

from bottle import route, template, get, run

import xmldict
import sys
import os
import codecs
import libxml2
import libxslt
from spellchecker import Spellchecker_si


@route('/')
@get('/spellcheck/<word>')
def spellcheck(word=u'<word>'):

    spellcheckedXML = Spellchecker_si().spellcheck(word, format='FULLXML')
    word = xmldict.xml_to_dict(spellcheckedXML)
    
    return template('INPUT WORD {{word}}', word=word)


run(host='localhost', port=8080, debug=True)
