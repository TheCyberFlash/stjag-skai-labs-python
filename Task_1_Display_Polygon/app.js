// Fetch JSON polygon data
fetch("polygon.json")
  .then((response) => response.json())
  .then((data) => {
    // Log the polygon coordinates
    console.log("Coordinates:", data.polygon);

    // Convert coordinates to the appropriate projection
    const polygonCoordinates = data.polygon.map((coordinate) =>
      ol.proj.fromLonLat(coordinate)
    );

    // Create a Polygon feature with the converted coordinates
    const polygon = new ol.Feature({
      geometry: new ol.geom.Polygon([polygonCoordinates]),
    });

    // Log the created Polygon feature and its extent
    console.log("Polygon Feature:", polygon);
    console.log("Polygon Extent:", polygon.getGeometry().getExtent());

    // Create a new source and layer for the Polygon
    const vectorSource = new ol.source.Vector({
      features: [polygon],
    });

    const vectorLayer = new ol.layer.Vector({
      source: vectorSource,
    });

    // Create a map with an OSM base layer and the Polygon layer
    const map = new ol.Map({
      target: "map", // HTML element to render the map
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM(), // OSM base layer
        }),
        vectorLayer, // Polygon layer
      ],
      view: new ol.View({
        center: ol.extent.getCenter(polygon.getGeometry().getExtent()), // Center the map on the extent of the Polygon
        zoom: 8, // Default zoom level
      }),
    });

    // Fit the view to the extent of the polygon to ensure it's visible
    map.getView().fit(polygon.getGeometry().getExtent(), map.getSize());

    // Log the created map
    console.log("Map:", map);
  })
  .catch((error) => console.error("Error:", error));
