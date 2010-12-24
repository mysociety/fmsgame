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
  autolocate_text = $("#autolocate_text").attr('value')

  if ( !!navigator.geolocation ) {
    $("#autolocate_ui")
        .html('<a href="#" onclick="lookup_location();return false">' + autolocate_text + '</a>');
  } else {
    $("#autolocate_ui")
        .html("Your browser does not support geolocation.");
  }
} );
