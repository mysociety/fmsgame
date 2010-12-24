function lookup_location() {
  $("#autolocate_ui").html("Trying to find you... please be patient... ");
  geo_position_js.getCurrentPosition( geolocation_success, display_geolocation_error );
}

function geolocation_success(loc) {

  $("#autolocate_ui")
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
    $("#autolocate_ui")
    .html('<a href="'+google_map_url+'">Found you - follow this link, choose "complete action using maps", then using the map walk to a nearby report. Once there tap the pin on the map and follow the link.</a>');

}

function display_geolocation_error() {
  $("#autolocate_ui")
    .html('Unable to determine your location.');
}

$(document).ready( function() {
  if ( geo_position_js.init() ) {
    $("#autolocate_ui")
        .html('<a href="#" onclick="lookup_location();return false">Locate me now!</a>');
  } else {
    $("#autolocate_ui")
        .html("Your browser does not support geolocation.");
  }
} );
