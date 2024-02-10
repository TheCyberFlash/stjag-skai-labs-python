// Fetch JSON polygon.json
fetch("polygon.json")
  .then((response) => response.json())
  .then((data) => {
    // Create a Polygon
    const polygon = new ol.Feature({
      geometry: new ol.geom.Polygon(data.coordinates),
    });

    //Create a new source and layer
    const vectorSource = new ol.source.Vector({
      features: [polygon],
    });

    const vectorLayer = new ol.layer.Vector({
      source: vectorSource,
    });

    // Create a map
    const map = new ol.Map({
      target: "map",
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM(),
        }),
        vectorLayer,
      ],
      view: new ol.View({
        center: ol.extent.getCenter(polygonFeature.getGeometry().getExtent()),
        zoom: 4,
      }),
    });

    console.log(polygon);
  })
  .catch((error) => console.error("Error:", error));

// Create a Polygon
// Create a map
// Bon Appétit!
