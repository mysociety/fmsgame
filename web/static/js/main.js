function lookup_location() {
  $("#message").html("Trying to find you...");
  geo_position_js.getCurrentPosition( geolocation_success_redirect, display_geolocation_error );
}

function geolocation_success_redirect(loc) {

  //var center = new GLatLng(loc.coords.latitude,loc.coords.longitude);

  var url
    = '/find_issues'
    + "?lon=" + loc.coords.longitude
    + "&lat=" + loc.coords.latitude;

  $("#message")
    .html('Found you - finding nearby issues');

  window.location = url;

}

function display_geolocation_error() {
  $("#message")
    .html('Unable to determine your location.');
}

$(document).ready( function() {
  if ( geo_position_js.init() ) {
    $("#autolocate")
        .html('<a href="#" onclick="lookup_location();return false">auto-locate</a>');
  } else {
    $("#message")
        .html("Your browser does not support geolocation.");
  }
} );
