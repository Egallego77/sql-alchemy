# Import everything you used in the starter_climate_analysis.ipynb file, along with Flask modules

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func,
import numpy as np
import pandas as pd


#################################################
# Database Setup
#################################################
# Create an engine
engine = create_engine("sqlite:///data/hawaii.sqlite")

# reflect an existing database into a new model using automap_base()

Base = automap_base()

# reflect the tables with Base.prepare(), passing in the engine and reflect=True
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Instantiate a Session and bind it to the engine

session = Session(bind=engine)

#################################################
# Flask Setup

from flask import Flask, jsonify


#################################################
# Instantiate a Flask object at __name__, and save it to a variable called app

app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Set the app.route() decorator for the base '/'
@app.route("/")
# define a welcome() function that returns a multiline string message to anyone who visits the route
def home():
    return (
        f"Welcome everyone to the Climate analysis App!<br />"
        f"Available routes<br />"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )
# Set the app.route() decorator for the "/api/v1.0/precipitation" route

@app.route("/api/v1.0/precipitation")

    

# define a precipitation() function that returns jsonified precipitation data from the database
def precipitation():
   # Create a session
   session = Session(bind=engine)
   
   # Calculate the date 1 year ago from last date in database
    last_date = (session
        .query(Measurement.date)
        .order_by(Measurement.date.desc())
        .first().date)

    # Calculate the date 1 year ago from last date in database
    One_Year_ago = dt.datetime.strptime(last_date, '%Y-%m-%d') -dt.timedelta(days=365)
    # Query for the date and precipitation for the last year

    rain_past_year = (session
        .query(Measurement.date, func.avg(Measurement.prcp))
        .filter(Measurement.date >= One_Year_ago)
        .group_by(Measurement.date).all())
    print(rain_past_year)
  # Create a dictionary to store the date: prcp pairs. 
  # Return the jsonify() representation of the dictionary
    return jsonify(rain_past_year)

    
# Set the app.route() decorator for the "/api/v1.0/stations" route
@app.route("/api/v1.0/stations")

# define a stations() function that returns jsonified station data from the database

def station():
  
   # Create a session
   session = Session(bind=engine)

    # Query for the list of stations

 stations=  (session
 .query(Measurement.station, func.count(Measurement.prcp))
 .group_by(Measurement.station)
 .order_by(func.count(Measurement.prcp).desc())
 .all())

 stations

    # Unravel results into a 1D array and convert to a list
    # Hint: checkout the np.ravel() function to make it easier to convert to a list
    np.ravel(Temp_last)
    # Return the jsonify() representation of the list
return jsonify(stations)

# Set the app.route() decorator for the "/api/v1.0/tobs" route
@app.route("/api/v1.0/tobs")

# define a temp_monthly() function that returns jsonified temperature observations (tobs) data from the database

def temp_monthly()

 # Create a session
   session = Session(bind=engine)


    # Query the primary station for all tobs from the last year

    Temp_last_12m = (session
                     .query(Measurement.date, Measurement.station, Measurement.tobs)
                     .filter(Measurement.station == 'USC00519281')
                     .filter(Measurement.date >= One_Year_ago)

    
    # Unravel results into a 1D array and convert to a list

    # Hint: checkout the np.ravel() function to make it easier to convert to a list
    np.ravel(Temp_last_12m)

    
    # Return the jsonify() representation of the list
    return jsonify(Temp_last_12m)



 


