var map;
var infowindows = [];

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
            add_marker(m.lat, m.lng, m.description, m.url, m.kind, m.image_url);
        }
    }
}

function add_marker(lat, lng, title, url, kind, photo){
    var latlng = new google.maps.LatLng(lat, lng);
    var infowindow = new google.maps.InfoWindow({
        content: '<div class="div_map_infowindow"><a href="'+url+'" alt="'+title+'" title="'+title+'"><img src="' + photo + '" class="img_map_scaled"></a></div>'
    });
    infowindows.push(infowindow);
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        icon: "/images/marker_" + kind + ".png",
        title: title
    });
    google.maps.event.addListener(marker, 'mouseover', function(event){
        for (i in infowindows) {
            infowindows[i].close();
        }
        infowindow.open(map, marker);
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
