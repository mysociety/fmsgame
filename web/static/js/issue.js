var acceptable_distance = 50;

var watchID;
var geoLoc;

function showLocation(position) {
  var csrf_token = $("#csrfmiddlewaretoken").attr('value')
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;

  var you_lat_radians = (latitude/180)*Math.PI;
  var you_long_radians = (longitude/180)*Math.PI;

  var target_lat = $("#target_lat").attr('value');
  var target_long = $("#target_long").attr('value');

  var target_lat_radians = (target_lat/180)*Math.PI;
  var target_long_radians = (target_long/180)*Math.PI;

  var long_difference = you_long_radians-target_long_radians;

  var issue_distance = distance(target_lat_radians, you_lat_radians, long_difference); // in metres

  $("#issue_distance")
    .html(issue_distance.toFixed(0) + '</strong> metres');

  if (issue_distance<acceptable_distance) {
    $("#can_we_fix_it")
      .html('<p>\
            You can <strong>win points</strong>\
            by choosing an option below!\
        </p>\
\
        <p>I think this problem is:</p>\
\
        <form action="" method="post">\
            <div style="display:none;"><input type="hidden"  name="csrfmiddlewaretoken" value="' + csrf_token + '" /></div>\
            <input type="hidden" name="state" value="fixed">\
            <input type="submit" value="FIXED" />\
        </form>\
        \
        <form action="" method="post">\
            <div style="display:none;"><input type="hidden"  name="csrfmiddlewaretoken" value="' + csrf_token + '" /></div>\
            <input type="hidden" name="state" value="notfixed">\
            <input type="submit" value="NOT FIXED" />\
        </form>\
        \
        <form action="" method="post">\
            <div style="display:none;"><input type="hidden"  name="csrfmiddlewaretoken" value="' + csrf_token + '" /></div>\
            <input type="hidden" name="state" value="notfound">\
            <input type="submit" value="CAN\'T FIND" />\
        </form>\
\
        <img src="/static/fmsgame_trophy.png" alt="FixMyStreet Game" style="margin-top:1em;">\
')
  }
  else {
    $("#can_we_fix_it")
      .html('Not close enough yet!')
  }

}

function errorHandler(err) {
  if(err.code == 1) {
    alert("Error: Access is denied!");
  }else if( err.code == 2) {
    alert("Error: Position is unavailable!");
  }
}
function getLocationUpdate(){
   if(navigator.geolocation){
      // timeout at 60000 milliseconds (60 seconds)
      var options = {timeout:60000};
      geoLoc = navigator.geolocation;
      watchID = geoLoc.watchPosition(showLocation, 
                                     errorHandler,
                                     options);
   }else{
      alert("Sorry, browser does not support geolocation!");
   }
}

$(document).ready( function() {
    getLocationUpdate()
  }
);
