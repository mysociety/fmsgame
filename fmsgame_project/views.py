from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
import fixmystreet
import datetime
import GeoRSS

@login_required
def issue(request, issue_id=None):
    if request.method == 'POST':
        state = request.POST.get('state')
        if state == 'fixed':
            pass
        elif state == 'notfixed':
            pass
        elif state == 'notfound':
            pass
        else:
            raise Http404
        return HttpResponseRedirect(reverse('geolocate'))
    return render_to_response('issue.html')

def find_issues(request):

    lat = request.REQUEST.get('lat')
    lon = request.REQUEST.get('lon')

    if lat is None or lon is None:
        raise Http404
        
    # We have a lat and lon - get the nearest issue from FixMyStreet and send the
    # user to it
    nearby_issues = fixmystreet.find_nearby_issues( lat=lat, lon=lon )

    rss_items = []
    
    for issue in nearby_issues:

        issue_url = request.build_absolute_uri( '/issue/' + str(issue['id']) )

        item = GeoRSS.GeoRSSItem(
            title        = issue['name'],
            link         = issue_url,
            description  = '<a href="' + issue_url + '">Check this issue</a>',
            guid         = GeoRSS.Guid( issue_url ),
            pubDate      = datetime.datetime.now(),    # FIXME
            geo_lat    = str(issue['lat']),
            geo_long   = str(issue['lon']),
        )


        rss_items.append( item )

    rss = GeoRSS.GeoRSS(
        title         = "Andrew's PyRSS2Gen feed",
        link          = request.build_absolute_uri(),
        description   = "Foo",
        lastBuildDate = datetime.datetime.now(),
        items         = rss_items,
    )
    
    return HttpResponse(
        content = rss.to_xml(),
        content_type = 'application/rss+xml'
    )
