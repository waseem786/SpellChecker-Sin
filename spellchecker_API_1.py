# -*- coding: utf-8 -*-
from bottle import route, template, get, run,post
import bottle
#import xmltodict
import sys
import os
import codecs
import libxml2
from spellchecker import Spellchecker_si
from beaker.middleware import SessionMiddleware
from cork import Cork
from cork.backends import MongoDBBackend
import logging
import webbrowser




  
@bottle.route('/spellcheck/<word>')

def spellcheck(word):
    #print 'remote_addr', bottle.request.remote_addr
    word = word.decode('utf-8')
    
    webbrowser.open('http://localhost/User%20confirmation/View/index.php')
    
    if word:
        json_output = Spellchecker_si().spellcheck(word, format='JSON')
        
    else:
        xml_output = "<spellcheck-result> <error> NO INPUT OR INVALID WORD </error> </spellcheck-result>"

        
    #json_output = xmltodict.parse(xml_output)
    return json_output
    #return xml_output


bottle.run(host='localhost', port=8080, debug=True)
