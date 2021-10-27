from flask import Flask, request, jsonify

app = Flask(__name__)

name = [
    {
        "id": 1, "name": "Raja", "done": False
    }, 
    {
        "id": 2, "name": "Rahul", "done": False
    }
]

@app.route("/add", methods = ["POST"])
def add_name():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the name"
        })
    
    t = {
        "id": name[-1]['id']+1,
        "title": request.json['title'],
        "done" : False
    }

@app.route("/get")
def get_name():
    return jsonify({
        "data": name
    })

if( __name__ == "__main__"):
    app.run(debug=True)