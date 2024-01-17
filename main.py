from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["sustainable_hub"]

# Define endpoint for community data management
@app.route("/community", methods=["GET", "POST"])
def manage_community_data():
    if request.method == "GET":
        # Retrieve community data
        community_data = list(db.community.find())
        return jsonify({"community_data": community_data})

    elif request.method == "POST":
        # Add new community data
        new_data = request.json
        db.community.insert_one(new_data)
        return jsonify({"message": "Community data added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
