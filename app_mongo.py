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
# Define the 'Economics' database in Mongo
db = client.mars_db
db.mars.drop()

db.mars.insert_many(
        [{'News_Title': "Alabama High School Student Names NASA's Mars Helicopter",\
             'News_Paragraph': "Vaneeza Rupani's essay was chosen as the name for the small spacecraft, which will mark NASA's first attempt at powered flight on another planet.", 'JPL_Featured_Image_URL': 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA16565_ip.jpg', 'Mars_Weather': 'InSight sol 519 (2020-05-12) low -92.3ºC (-134.2ºF) high -0.3ºC (31.4ºF)\nwinds from the SW at 4.7 m/s (10.4 mph) gusting to 15.8 m/s (35.3 mph)\npressure at 7.00 hPa', 'Mars_Facts': '<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Value</th>    </tr>\
 <tr>      <th>Description</th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>Equatorial Diameter:</th>      <td>6,792 km</td>    </tr>    <tr>      <th>Polar Diameter:</th>      <td>6,752 km</td>    </tr>    <tr>      <th>Mass:</th>      <td>6.39 × 10^23 kg (0.11 Earths)</td>    </tr>    <tr>      <th>Moons:</th>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>Orbit Distance:</th>      <td>227,943,824 km (1.38 AU)</td>    </tr>    <tr>      <th>Orbit Period:</th>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>Surface Temperature:</th>      <td>-87 to -5 °C</td>    </tr>    <tr>      <th>First Record:</th>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>Recorded By:</th>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>', 'Mars_Hemispheres': [{'title': 'Cerberus Hemisphere\
Enhanced', 'img_url': 'https://astrogeology.usgs.gov//cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov//cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov//cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov//cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]}
        ]
)
