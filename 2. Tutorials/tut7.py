import json
import os
from bottle import route, run, , request

config_file = open( 'config.json' )
config_data = json.load( config_file )
pth_xml     = config_data["paths"]["xml"]

@route('/recipes/<name>', method='DELETE' )
def recipe_delete( name="" ):
    if "" != name:
        try:
            os.remove( os.path.join( pth_xml, name + ".xml" ) )
            return { "success" : True  }
        except:
            return { "success" : False  }
