# Importing Necessary Modules
import requests
from selenium import webdriver
import folium
import datetime
import time
import os

# This method will return the user's actual coordinates using their IP address
def locationCoordinates():
    try:
        # Fetching geolocation data based on IP address
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except requests.RequestException:
        # Error handling for issues with network or API request
        print("Internet Not Available. Please check your connection.")
        exit()

# This method will fetch the coordinates and create an HTML file of the map
def gps_locator():
    try:
        lat, long, city, state = locationCoordinates()

        # Print location data to the console
        print(f"You Are in {city}, {state}")
        print(f"Your latitude = {lat} and longitude = {long}")

        # Create a map object centered at the user's location
        obj = folium.Map(location=[lat, long], zoom_start=12)

        # Adding a marker for the current location
        folium.Marker([lat, long], popup='Current Location').add_to(obj)

        # Generate the file name with the current date
        file_path = os.path.join(os.getenv('USERPROFILE'), 'Downloads', f'prac14html_{datetime.date.today()}.html')

        # Save the map to an HTML file
        obj.save(file_path)
        
        return file_path

    except Exception as e:
        # Error handling for any issue with map creation
        print(f"An error occurred: {str(e)}")
        return None

# Main method
if __name__ == "__main__":
    print("---------------GPS Using Python---------------\n")

    # Call the gps_locator function to generate the map and open the file in Chrome
    page = gps_locator()

    if page:
        print("\nOpening File.............")
        try:
            # Open the generated HTML file in a Chrome browser
            dr = webdriver.Chrome()
            dr.get(f"file:///{page}")
            time.sleep(20)
            dr.quit()
            print("\nBrowser Closed..............")
        except Exception as e:
            print(f"Failed to open the browser: {str(e)}")
    else:
        print("Failed to create the map HTML file.")
