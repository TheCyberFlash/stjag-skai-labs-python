fetch("polygon.json")
  .then((response) => response.json())
  .then((data) => {
    console.log("Coordinates:", data.polygon);

    const polygonCoordinates = data.polygon.map((coordinate) => ol.proj.fromLonLat(coordinate));

    // Create a Polygon
    const polygon = new ol.Feature({
      geometry: new ol.geom.Polygon([polygonCoordinates]),
    });

    console.log("Polygon Feature:", polygon);
    console.log("Polygon Extent:", polygon.getGeometry().getExtent());

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
        zoom: 10, 
      }),
    });

    console.log("Map:", map);
  })
  .catch((error) => console.error("Error:", error));
