from flask import Flask
from flask import Response
from src.wakeonlan import wakeonlan


app = Flask(__name__)

@app.route('/wake/<target>', methods=['GET'])
def wake(target):
    wol = wakeonlan()
    wol.wake(target)
    return Response(status=200)
    

@app.route('/ping', methods=['GET'])
def ping(target):
	response = Flask.make_response("OK", 200)
	response.mimetype = "text/plain"
	return response
    

if __name__ == '__main__':
    app.run(debug=True)