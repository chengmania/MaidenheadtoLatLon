#Code by Chengmania written on a Sunday in October 2024
#Code Updated and enhanced by Chris later that week
#This code is free for use, modifcation, and enhanced

from flask import Flask, render_template, request
import maidenhead as mh
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

app = Flask(__name__)


@app.route('/city', methods=['GET', 'POST'])
def citytogrid():
    lat1 = lon1 = lat2 = lon2 = None
    grid1 = grid2 = distance = None
    error = None

    if request.method == 'POST':
        city  = request.form.get('city',  '').strip().upper()

        if city:
            try:

                # instantiate a new Nominatim client
                app = Nominatim(user_agent="tutorial")

                # get location raw data
                location = app.geocode(city).raw

                latitude = location["lat"]
                longitude = location["lon"]
                #print(f"Coordinates and grid location for {city}:\n{latitude}, {longitude}")

                # Level Precision
                # 1     World           AA
                # 2     Regional        AA11
                # 3     Metropolis      AA11aa
                # 4     City            AA11aabb
                level = 3

                gridloc = mh.to_maiden(float(latitude), float(longitude), level)
                #print(f"{gridloc}")
                return render_template('index.html', cityname=city, lat1=latitude, lon1=longitude, lat2=latitude, lon2=longitude, gridc=gridloc, error=error)

            except ValueError as e:
                error = f"Error: {e}. Please enter valid Maidenhead grid squares."
                return render_template('index.html', error=error, grid1=grid1, grid2=grid2)
        
    return render_template('index.html', lat1=lat1, lon1=lon1, lat2=lat2, lon2=lon2, grid1=grid1, grid2=grid2, distance=distance, error=error)
        


@app.route('/', methods=['GET', 'POST'])
def index():
    lat1 = lon1 = lat2 = lon2 = None
    grid1 = grid2 = distance = None
    error = None

    if request.method == 'POST':
        grid1 = request.form.get('grid1', '').strip().upper()
        grid2 = request.form.get('grid2', '').strip().upper()
        
        if not grid1 or not grid2:
            error = "Please enter both grid squares."
            return render_template('index.html', error=error, grid1=grid1, grid2=grid2)
        try:
            # Get center coordinates by setting center=True
            lat1, lon1 = mh.to_location(grid1, center=True)
            lat2, lon2 = mh.to_location(grid2, center=True)

            # Calculate distance in miles
            location1 = (lat1, lon1)
            location2 = (lat2, lon2)
            distance = geodesic(location1, location2).miles

        except ValueError as e:
            error = f"Error: {e}. Please enter valid Maidenhead grid squares."
            return render_template('index.html', error=error, grid1=grid1, grid2=grid2)
    return render_template('index.html', lat1=lat1, lon1=lon1, lat2=lat2, lon2=lon2, grid1=grid1, grid2=grid2, distance=distance, error=error)

if __name__ == '__main__':
    app.run(debug=True)
