from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
# mongo = PyMongo(app)

#Create a connection to a local MongoDB database
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

db = client.mars_app
db.mars.drop()



# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars_info=mars)


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape_mars.All()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
