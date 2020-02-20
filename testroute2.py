from run import app

@app.route('/testing2')
def testing2():
    return 'it works also!'