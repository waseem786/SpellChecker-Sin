import bottle
import bottle_mysql
from bottle import route, run
import MySQLdb

app = bottle.Bottle()
# dbhost is optional, default is localhost
plugin = bottle_mysql.Plugin(dbuser='user_name', dbpass='user_pass', dbname='dbtest')
app.install(plugin)

def check(dbuser, passwd):
      if dbuser == user_name:

        return True

@bottle.route('/show/:<tem>')
@bottle.auth_basic(check)
def show(item, dbtest):
    db.execute('SELECT * from items where name="%s"', (item,))
    row = db.fetchone()
    if row:
        return template('showitem', page=row)
    return HTTPError(404, "Page not found")


run(host='localhost', port = 8080, debug= True )
