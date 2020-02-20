from run import app
from run import a

b = a
b.foo()

@app.route('/testing')
def testing():
    return 'it works!'