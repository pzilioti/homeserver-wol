from flask import Flask
from flask import Response
from src.wakeonlan import wakeonlan


app = Flask(__name__)

@app.route('/wake/<target>', methods=['GET'])
def wake(target):
    wol = wakeonlan()
    wol.wake(target)
    return Response(status=200)
    

if __name__ == '__main__':
    app.run(debug=True)