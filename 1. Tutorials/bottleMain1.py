# bottleMain1.py

app = Bottle(); 

@app.route('/')
def hello():
    return 'Hello World'

app.run()
