from flask import *

app  = Flask(__name__)

@app.route('/')  
def home():
    return "Hi P'Pream"
    
if __name__ == '__main__':
    app.run() 
