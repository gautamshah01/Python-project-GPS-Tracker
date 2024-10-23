<h1 align=center>🌍 GPS Locator Using Python</h1>

This project is a simple yet powerful GPS locator tool built using Python. It leverages IP-based geolocation to determine the user's current coordinates (latitude and longitude) and displays the location on an interactive map using the folium library. The project also automates the opening of this map in a browser using the selenium library.


<h2>🚀 Features</h2>

IP-Based Geolocation: Fetches your current location using IP address via the ipinfo.io API.

Interactive Map: Automatically generates a visually appealing map with a marker at your location using folium.

Browser Automation: Opens the map in a Chrome browser using Selenium, allowing for a seamless, automated experience.

User-Friendly: The map is saved as an HTML file and is easily shareable or accessible later.

<h2>🛠️ Installation</h2>

Install the Dependencies: Install the required Python libraries using pip:


pip install requests selenium folium
Install ChromeDriver:

Download and install ChromeDriver, ensuring it matches the version of your installed Chrome browser.
Add ChromeDriver to your system PATH, or specify its location in your code.

<h2>💻 Usage</h2>

After cloning the repository and installing dependencies, you can run the script as follows:


python gps_locator.py
What the Script Does:
Fetch Location: The script fetches your current location based on your public IP address using the ipinfo.io service.
Generate Map: It generates an HTML file that contains a map with a marker indicating your current location.
Open Map in Browser: It automatically opens this HTML file in a Chrome browser using Selenium for easy viewing.
Example Output
The terminal will output your location data:


---------------GPS Using Python---------------

You Are in Mumbai, Maharashtra
Your latitude = 19.0728 and longitude = 72.8826

Opening File.............
The generated HTML map file will then open in a browser.

<h2>📁 HTML File Generation</h2>

The generated HTML file is saved in your local Downloads directory by default, with a filename in the format prac14html_<DATE>.html. You can modify the file path in the code to store it in a different location.

Example File Path
plaintext
Copy code
C:/Users/navin/Downloads/prac14html_2024-08-23.html

<h2>🔍 Code Explanation</h2>

locationCoordinates()
This function sends a request to ipinfo.io to retrieve geolocation data (latitude, longitude, city, and state) based on your public IP address.
Returns the latitude, longitude, city, and state for use in the map generation.
gps_locator()
Uses the folium library to create a map centered on the coordinates retrieved from locationCoordinates().
Adds a marker to the map to pinpoint the exact location.
Saves the generated map as an HTML file.
Browser Automation
The Selenium webdriver.Chrome() function is used to open the generated HTML map file automatically in a Chrome browser.
After 20 seconds, the browser will automatically close.


<h2>🧩 Prerequisites</h2>

Python 3.x: Ensure Python 3.x is installed on your machine.

Google Chrome: The script automates Chrome for displaying the map, so Chrome must be installed.

ChromeDriver: Ensure that ChromeDriver is installed and properly configured.


<h2>⚙️ Customization</h2>

Feel free to modify the following parts of the code for further customization:

Map Location: Modify the map location or zoom level by adjusting the latitude, longitude, and zoom settings in the folium.Map() function.

Marker and Popup: You can customize the marker popup message or add more details (like additional markers).

File Path: Change the path where the HTML file is saved by modifying the fileName variable in the gps_locator() function.

<h2>🛡️ Error Handling</h2>

The script includes basic error handling, such as:

Internet Unavailability: If there is no internet connection, the script will exit gracefully with a message.

Browser Issues: If Selenium encounters issues (e.g., incorrect file path or missing ChromeDriver), the error will be printed to the console for debugging.


<h2>📜 Future Improvements</h2>

GUI(Graphical User Interface): Implement a GUI for easier interaction.

Multiple Location Markers: Extend the functionality to add multiple location markers on the map.

Cross-Browser Support: Add support for other browsers like Firefox or Edge by using their respective web drivers.


<h2>🏆 License</h2>

This project is licensed under the MIT License - see the LICENSE file for more details.


<h2>🤝 Contributions</h2>

Feel free to fork the repository and submit pull requests. All contributions are welcome!

<h2>🔗 Links</h2>

Documentation: Folium Library

Selenium Documentation: Selenium WebDriver for Python

IPInfo API: ipinfo.io


<h2>📧 Contact</h2>

If you have any questions or suggestions, feel free to open an issue or contact me directly.

