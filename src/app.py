from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


@app.route('/message', methods=['POST'])
def route_message():
    if request.method == 'POST':
        request_data = request.get_json()
        message = request_data['message']
        response = json.dumps({'message': message})
        return response


if __name__ == "__main__":
    app.run()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
