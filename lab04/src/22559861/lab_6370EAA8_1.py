from flask import Flask, jsonify
app=Flask(__name__)

# Redirect to our Home page
@app.route('/')
def index():
    return "Hello World"
# Return json data for this url
@app.route('/api/v1/teachingplan', methods=['GET'])
def get_books():
    return jsonify({"teachingplan":teachingplan})
# Return a subset of json data if a more specific url p
@app.route('/api/v1/teachingplan/<int:id>', methods=['GET'])
def get_book(id):
    ch= [ch for ch in teachingplan if ch['id'] ==id]
    return jsonify({'ch': ch})

teachingplan=[
    {
        "id":0,
        "title":"Course overview and Introduction",
    },
    {
        "id":1,
        "title":"Basic Elements",
    },
    {
        "id":2,
        "title":"Data Types",
    },
    {
        "id":3,
        "title":"Development Tools",
    },
    {
        "id":4,
        "title":"Control flow (1)",
    }
    ]
    
if __name__=="__main__":app.run(debug=True)
