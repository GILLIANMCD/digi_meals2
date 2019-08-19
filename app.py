import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "digi_meals"
COLLECTION_NAME = "recipes"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipe.html", task=mongo.db.recipe.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)