from flask import Flask 

app = Flask(__name__) 

@app.route('/') 

def index(): 

    return '1st chatting history clear chey prathi roju ' 

if __name__ == '__main__': 

    app.run(host='0.0.0.0', port=8080) 

 
