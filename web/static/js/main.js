function lookup_location() {
  $("#message").html("Trying to find you...");
  geo_position_js.getCurrentPosition( geolocation_success_redirect, display_geolocation_error );
}

function geolocation_success_redirect(loc) {

  $("#message")
    .html('Found you - finding nearby issues');

  var rss_url
    = 'http://'
    + window.location.host
    + '/find_issues'
    + "?lon=" + loc.coords.longitude
    + "&lat=" + loc.coords.latitude;

  var google_map_url
   = 'http://maps.google.com/maps?q=' + escape( rss_url );

  // window.location = google_map_url;

  // Note - we need to display the url for the ser to click on so that the smart
  // phones offer the user the choice to use the map app rather than the web page.
    $("#message")
    .html('<a href="'+google_map_url+'">Found you - click me to view nearby issues</a>');

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
