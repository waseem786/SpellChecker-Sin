import json
import os
from bottle import route, run

config_file = open( 'config.json' )
config_data = json.load( config_file )
pth_xml     = config_data["paths"]["xml"]

@route('/recipes/')
def recipes_list():
    paths = []
    ls = os.listdir( pth_xml )
    for entry in ls:
        if ".xml" == os.path.splitext( entry )[1]:
            paths.append( entry )
    return { "success" : True, "paths" : paths }
