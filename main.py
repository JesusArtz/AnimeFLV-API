from __init__ import app
from src import ROOT

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
for route in ROOT:
    app.add_url_rule(route['path'], route['endpoint'], route['function'], methods=[route['method']])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)