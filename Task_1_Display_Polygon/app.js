fetch("polygon.json")
  .then((response) => response.json())
  .then((data) => {
    console.log("Coordinates:", data.polygon);

    // Create a Polygon
    const polygon = new ol.Feature({
      geometry: new ol.geom.Polygon([data.polygon]),
    });

    console.log("Polygon Feature:", polygon);

    // Create a new source and layer
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
        center: ol.extent.getCenter(polygon.getGeometry().getExtent()),
        zoom: 4,
      }),
    });

    console.log("Map:", map);
  })
  .catch((error) => console.error("Error:", error));
