from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
      "Content-Type": "application/json",
      "Answer":{"Text": answer}
    }
    # return answer
    return jsonify(result)

@app.route('/reply2', methods=['POST'])
def reply2():
    data = json.loads(request.data)
    d_str = str(data['string'])
    d_num = int(data['num'])
    # ast使わずに素直にsplitでリスト化したほうが楽
    d_list = data['list'].split(',')
    # d_list = ['AA', 'BC']
    
    result = {
        "Content-Type": "application/json",
        "Input":{"string": d_str, "num": d_num, "list": d_list},
        "Types":{"string": str(type(d_str)), "num": str(type(d_num)), "list": str(type(d_list))}
    }
    return jsonify(result)

if __name__ == "__main__":
    # app.run(host='0.0.0.0',port=12345,debug=True)
    app.run(port=12345,debug=True)