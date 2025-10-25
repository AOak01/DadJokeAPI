from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_joke():
    joke = "Why don't skeletons fight each other? They don't have the guts."
    return jsonify({"joke": joke})

if __name__ == '__main__':
    app.run(debug=True)