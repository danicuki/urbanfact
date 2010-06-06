var map;

function load_map(){
    city_center = new google.maps.LatLng(-23.548153, -46.633101);
    map = new google.maps.Map(document.getElementById("map_canvas"), {
        zoom: 13,
        scaleControl: true,
        center: city_center,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
}

function add_marker(lat, lng){
	latlng = new Array(lat, lng);
    marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, lng),
        map: map,
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
