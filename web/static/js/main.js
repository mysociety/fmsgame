function lookup_location() {
  $("#autolocate_ui").html("Trying to find you... please be patient... ");
  navigator.geolocation.getCurrentPosition( geolocation_success, display_geolocation_error );
//  geo_position_js.getCurrentPosition( geolocation_success, display_geolocation_error );
}

function geolocation_success(loc) {
  window.location.replace('/located?lon=' + loc.coords.longitude + '&lat=' + loc.coords.latitude)
}

function display_geolocation_error() {
  $("#autolocate_ui")
    .html('Unable to determine your location.');
}

$(document).ready( function() {
  if ( !!navigator.geolocation ) {
    $("#autolocate_ui")
        .html('<a href="#" onclick="lookup_location();return false">Locate me now!</a>');
  } else {
    $("#autolocate_ui")
        .html("Your browser does not support geolocation.");
  }
} );
