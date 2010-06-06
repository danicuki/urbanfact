var map;

function load_map(){
    city_center = new google.maps.LatLng(-23.548153, -46.633101);
    map = new google.maps.Map(document.getElementById("map_canvas"), {
        zoom: 13,
        scaleControl: true,
        center: city_center,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    for (i in markers) {
        var m = markers[i];
        if (m && m.lat) {
            add_marker(m.lat, m.lng, m.description, m.url);
        }
    }
}

function add_marker(lat, lng, title, url){
    var latlng = new google.maps.LatLng(lat, lng);
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: title
    });
    google.maps.event.addListener(marker, 'click', function(event) {
	    window.location.href = url;		
	});
}

function adjust_map_height(){
    n = $(document).height() - 125;
    $(".div_map").css("height", n + "px");
}

$(document).ready(function(){
    adjust_map_height();
    load_map();
    $(window).resize(function(){
        adjust_map_height();
    });
});
