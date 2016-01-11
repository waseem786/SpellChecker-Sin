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
def spellcheck(word=word):

    xml_output = Spellchecker_si().spellcheck(word, format='FULLXML')
    json_outout = xmldict.xml_to_dict(xml_output)
    
    return xml_output


run(host='localhost', port=8080, debug=True)
