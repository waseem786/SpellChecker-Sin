# -*- coding: utf-8 -*-

from bottle import route, template, get, run

#import xmltodict
import sys
import os
import codecs
import libxml2
from spellchecker import Spellchecker_si


@route('/spellcheck/<word>')
def spellcheck(word):
    word = word.decode('utf-8')
    if word:
        xml_output = Spellchecker_si().spellcheck(word, format='JSON')
    else:
        xml_output = "<spellcheck-result> <error> NO INPUT OR INVALID WORD </error> </spellcheck-result>"
    #json_output = xmltodict.parse(xml_output)
    
    #return json_output
    return xml_output


run(host='localhost', port=8080, debug=True)

