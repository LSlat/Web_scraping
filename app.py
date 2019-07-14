#Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Create connection variable 
# conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
# client = pymongo.MongoClient(conn)
    #The above line gives an error, 'pymongo is not defined'

# Connect to a database. Will create one if not already available.
db = client.mars_db
    #error message: name 'client' is not defined

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    mars_data = mongo.db.collection.find()

    #Return template and data
    return render_template("index.html", mars_data=mars_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


