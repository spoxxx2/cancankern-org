#!/bin/bash
cat << 'HTML' > index.html
<!DOCTYPE html>
<html>
<head>
    <title>Cancan Kern - Golden Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>#map { height: 600px; width: 100%; border-radius: 15px; }</style>
</head>
<body>
    <h1>Bakersfield Digital Twin - Live Audit Map</h1>
    <div id="map"></div>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        var map = L.map('map').setView([35.3733, -119.0187], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
        
        // Data points will be injected here
        var points = [
HTML

# Extracting coordinates from your JSON and formatting for JS
grep -oP 'lat":\K[0-9.-]+|lon":\K[0-9.-]+' data/map_points.json | paste -d, - - | awk -F, '{print "            L.marker([" $1 ", " $2 "]).addTo(map).bindPopup(\"Golden Audit Secure\");"}' >> index.html

cat << 'HTML' >> index.html
        ];
    </script>
</body>
</html>
HTML
echo "Map generated in index.html"
