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
import MySQLdb
import pymysql
import mysql.connector
import hashlib


def check(user, passwd):
    
    db = MySQLdb.connect("localhost","root","","mysitedb")
    cursor = db.cursor()
    cursor.execute("SELECT email, password \
                FROM s_user \
                WHERE email = '%s'" % user)

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    # Conver to MD5 hash
    hashpass = hashlib.md5(passwd).hexdigest()
                   
    if (data and user==data[0] and hashpass==data[1]):
        db.close()
        return True
    db.close()
    return False
  
@bottle.route('/spellcheck/<word>')
@bottle.auth_basic(check)

def spellcheck(word):
    print 'auth', bottle.request.auth
    print 'remote_addr', bottle.request.remote_addr
    word = word.decode('utf-8')
    
    if word:
        json_output = Spellchecker_si().spellcheck(word, format='JSON')    
    else:
        xml_output = "<spellcheck-result> <error> NO INPUT OR INVALID WORD </error> </spellcheck-result>"
        
    #json_output = xmltodict.parse(xml_output)
    #return xml_output
    return json_output

run(host='localhost', port=8080, debug=True)
