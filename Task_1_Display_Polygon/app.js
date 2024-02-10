// Fetch JSON polygon.json
fetch("polygon.json")
  .then((response) => response.json())
  .then((data) => {
    // Create a Polygon
    const polygon = new ol.Feature({
      geometry: new ol.geom.Polygon(data.coordinates),
    });

    console.log(polygon);
  });

// Create a Polygon
// Create a map
// Bon Appétit!
