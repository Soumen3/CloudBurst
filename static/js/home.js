
//------------------Map insitialization--------------------//

var map = L.map('map').setView([20.5937, 78.9629], 4.5);


//----------------------Tile Layer-------------------------//

var osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
osm.addTo(map);


//---------------------Legend--------------------------//
var legend = L.control({ position: 'bottomright' });

legend.onAdd = function (map) {
    var div = L.DomUtil.create('div', 'info legend');
    div.innerHTML = document.getElementById('map-legend').innerHTML;
    return div;
};

legend.addTo(map);