from flask import Flask, render_template, request
import maidenhead as mh
from geopy.distance import geodesic

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize variables
    lat1 = lon1 = lat2 = lon2 = None
    grid1 = grid2 = distance = None
    error = None

    if request.method == 'POST':
        print("Form Data:", request.form)  # Debug statement
        grid1 = request.form.get('grid1', '').strip().upper()
        grid2 = request.form.get('grid2', '').strip().upper()
        if not grid1 or not grid2:
            error = "Please enter both grid squares."
            return render_template('index.html', error=error, grid1=grid1, grid2=grid2)
        try:
            lat1, lon1 = mh.to_location(grid1)
            lat2, lon2 = mh.to_location(grid2)

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
