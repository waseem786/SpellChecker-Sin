# -*- coding: utf-8 -*-

from bottle import route, template, get, run

import xmldict
import sys
import os
import codecs
import libxml2
from spellchecker import Spellchecker_si


@route('/spellcheck/<word>')
def spellcheck(word):
    word = word.decode('utf-8')
    if word:
        xml_output = Spellchecker_si().spellcheck(word, format='TEXT')
    else:
        xml_output = "No input word."
    #json_output = xmldict.xml_to_dict(xml_output)

    return xml_output


run(host='localhost', port=8080, debug=True)
