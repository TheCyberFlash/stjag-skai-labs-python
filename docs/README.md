# [Github Page](https://thecyberflash.github.io/stjag-skai-labs-python/)

## Display Polygon on a Map

### Intro

This web application uses the OpenLayers library to display a polygon on a map. The polygon coordinates are fetched from the "polygon.json" file, and the map is rendered accordingly.

### Assumptions

Assume the polygon.json file contains valid geo-coordinates in the required format.

### Instructions

1. **Clone the Repository:**

   - Clone this repository to your local machine.

2. **Navigate to the Project Folder:**

   - Open a terminal and navigate to the project folder using the `cd` command.

3. **Start a Local Server:**

   - Start a simple Python web server by running the command:
     ```bash
     python -m http.server
     ```

4. **Open the Application:**
   - Open a web browser and visit [http://localhost:8000/index.html](http://localhost:8000/index.html).

### Additional Notes

- If any issues arise, ensure that the "polygon.json" file is present and contains valid geo-coordinates.
- Adjustments to the zoom level are automatically made to fit the entire polygon on the map.
- For more information, refer to the comments in the `app.js` file.
