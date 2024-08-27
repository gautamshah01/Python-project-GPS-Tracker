GPS Locator Using Python
This Python script utilizes IP-based geolocation to determine the current location's latitude and longitude. It then plots the location on an interactive map using the folium library and opens the map in a browser using selenium.

Features
Fetches Current Location: Uses the IP address to retrieve latitude and longitude coordinates, city, and state.
Creates Interactive Map: Generates an HTML file with a map centered on the user's current location and marks it with a pin.
Browser Automation: Opens the generated map in a Chrome browser using Selenium for visualization.
Requirements
Before running the script, ensure you have the following Python packages installed:

bash
Copy code
pip install requests selenium folium
Additionally, you need to have the ChromeDriver installed and configured to match your Chrome browser version.

Usage
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/gps-locator-python.git
cd gps-locator-python
Run the script:

bash
Copy code
python gps_locator.py
Output:

The script will fetch your current location and generate an HTML file with the map.
This file will be opened automatically in your browser using Selenium.
Code Overview
locationCoordinates()
This function uses the ipinfo.io API to retrieve the current latitude and longitude based on your public IP address. It returns the coordinates along with the city and state.

gps_locator()
This function creates a map centered on the retrieved coordinates using folium. A marker is added to the map at the current location, and the map is saved as an HTML file in your local directory.

Example Output
When you run the program, it will output:

plaintext
Copy code
---------------GPS Using Python---------------

You Are in Mumbai, Maharashtra
Your latitude = 19.0728 and longitude = 72.8826

Opening File.............
The generated map will open in your default browser with a marker indicating your current location.

File Path for HTML
By default, the HTML map file is saved in the Downloads directory with the filename prac14html<date>.html. You can customize the file path within the code.

Notes
The script is designed to work with an internet connection. If the internet is unavailable, it will gracefully exit with an error message.
Make sure you have the chromedriver executable in your PATH or specify its location in the code for Selenium to work properly.
Future Improvements
Add error handling for potential exceptions during file generation or browser automation.
Improve the UI of the generated map by adding more features, such as geolocation accuracy or multiple location pins.
Implement a GUI for easier interaction.
License
This project is licensed under the MIT License - see the LICENSE file for details.
