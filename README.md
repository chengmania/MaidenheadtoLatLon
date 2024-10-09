![image](https://github.com/user-attachments/assets/4230c6fb-5789-401f-a290-797e5f8c1736)


Maidenhead Grid Locator Web Application
This web application allows users to input two Maidenhead grid squares, displays their locations on an interactive map with markers, calculates the distance between them in miles, and draws a line connecting the two points.

Table of Contents\
Prerequisites\
Installation\
Project Structure\
Usage\
Example\
Notes\
Troubleshooting\
Contributing


Prerequisites
Python 3.6+ installed on your system.
pip (Python package installer).

Installation
Follow the steps below to set up and run the application:

1. Clone or Download the Repository
If you're using Git, you can clone the repository:

git clone https://github.com/chengmania/maidenhead-grid-locator.git
cd maidenhead-grid-locator

Alternatively, download the project files and navigate to the project directory.

2. Create a Virtual Environment (Optional but Recommended)
It's good practice to create a virtual environment to manage your project's dependencies.

        python -m venv venv
Activate the virtual environment:

On Windows:

        venv\Scripts\activate
On macOS and Linux:

        source venv/bin/activate

3. Install Required Python Packages
Install the necessary Python packages using pip:

        pip install flask maidenhead geopy

Flask: A lightweight web application framework.
maidenhead: A library for converting Maidenhead grid squares to latitude and longitude.
geopy: A library for calculating distances between geographic coordinates.

4. Download Marker Images
Download the marker images and place them in the static folder:

red_pin.png: Download here

green_pin.png: Download here

Save these images into the static directory within your project:

    maidenhead-grid-locator/
    ├── mtoll.py
    ├── templates/
    │   └── index.html
    └── static/
        ├── red_pin.png
        └── green_pin.png

5. Verify Project Structure
Your project directory should look like this:

        maidenhead-grid-locator/
        ├── mtoll.py
        ├── templates/
        │   └── index.html
        └── static/
            ├── red_pin.png
            └── green_pin.png

mtoll.py: The main Flask application.

templates/index.html: The HTML template for the web application.

static/: Directory containing static files like images.

Usage

Running the Application
Start the Flask application by running:


    python3 mtoll.py

If you're using a virtual environment, make sure it's activated.

Accessing the Application
Open your web browser and navigate to:

http://127.0.0.1:5000/

Example
Enter Maidenhead Grid Squares

On the webpage, enter two Maidenhead grid squares in the input fields. For example:

Grid Square 1: EM15
Grid Square 2: FN20
Submit the Form

Click on the "Show on Map" button.

View Results

The map will display both locations with red and green pins.
A blue line connects the two points.
The distance between the two grid squares is calculated and displayed in miles.

Notes
Grid Square Precision

The accuracy of the location depends on the length of the grid square code.
Longer grid squares (e.g., EM15aa) provide more precise locations.
Customizing the Map

You can adjust the zoom level and map center in the index.html file.
The line thickness can be adjusted by changing the weight property in the polyline options.
Error Handling

If invalid grid squares are entered, an error message will be displayed.
Ensure that the grid squares are valid and correctly formatted.
Dependencies

If you encounter issues with package installations, ensure that you have the latest version of pip.

    Use pip install --upgrade pip to update pip if necessary.
Troubleshooting
Common Issues

KeyError: 'grid1'

Cause: This error occurs when the key 'grid1' is not present in request.form, meaning the form did not submit a field named 'grid1'.

Solution: Ensure that the name attributes in your input fields are correctly set to grid1 and grid2 in index.html, and that the form's method is set to POST.

html

    <form method="POST">
        <label for="grid1">Enter Maidenhead Grid Square 1:</label>
        <input type="text" name="grid1" id="grid1" required>
        <br><br>
        <label for="grid2">Enter Maidenhead Grid Square 2:</label>
        <input type="text" name="grid2" id="grid2" required>
        <br><br>
        <input type="submit" value="Show on Map">
    </form>

Static Files Not Loading

Cause: The images (red_pin.png and green_pin.png) may not be found.
Solution: Verify that the images are correctly placed in the static directory and that the paths in index.html are correct.
Port Already in Use

Solution: If port 5000 is already in use, you can run the Flask app on a different port:


    python3 mtoll.py --port 5001
Then access the application at http://127.0.0.1:5001/.

Virtual Environment Issues

Solution: If you're having trouble with the virtual environment, you can run the application without it, but be cautious about package versions and dependencies.
Debugging Tips

Print Form Data

Add a print statement in your mtoll.py to see the form data being submitted:


    if request.method == 'POST':
        print("Form Data:", request.form)

Check the console output when submitting the form to ensure that grid1 and grid2 are present.

Browser Developer Tools

Use your browser's developer tools to inspect the network requests and ensure the form data is being sent correctly.

Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.
