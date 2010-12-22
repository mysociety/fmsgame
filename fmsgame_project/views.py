import urlparse
import urllib2
import urllib

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
import fixmystreet
import datetime
import GeoRSS

import settings

from BeautifulSoup import BeautifulSoup

@login_required
def issue(request, issue_id=None):
    if request.method == 'POST':
        target_url = urlparse.urljoin(settings.FMS_URL, '/report/%s' % issue_id)
        data =  {'submit_update': '1',
                 'id': issue_id,
                 'name': request.user.get_full_name(),
                 'rznvy': 'mysociety.director@gmail.com',  # request.user.email,
                 #'email': '', # check this
                 #'update': '', # text of the update (e.g., "I put it in the bin")
                 'fixed': '', # checkbox for: Is it fixed?
                 'add_alert': '', # don't add the user to automatic alert notifications
                 'photo': '', 
                }
        state = request.POST.get('state')
        if state == 'fixed':
            data['fixed'] = 1
            data['update'] = 'fmsgame: this is fixed'
        elif state == 'notfixed':
            data['update'] = 'fmsgame: this is not fixed'
        elif state == 'notfound':
            data['update'] = "fmsgame: this couldn't be found"
        else:
            raise Http404
        response = urllib2.urlopen(target_url, urllib.urlencode(data))
        # FIXME handle the response    
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

        description_start = '<a href="' + issue_url + '">Follow this link</a><br><br>'

        # Not sure why this is not working... should strip out the 'Report on FixMyStreet' link
        # description_end = ''.join(BeautifulSoup( issue['summary'] ).findAll( lambda tag: tag.name != 'a' ))

        description_end = ' '.join(BeautifulSoup( issue['summary'] ).findAll( text = True ))

        item = GeoRSS.GeoRSSItem(
            title        = issue['name'],
            link         = issue_url,
            description  = description_start + description_end,
            guid         = GeoRSS.Guid( issue_url ),
            pubDate      = datetime.datetime.now(),    # FIXME
            geo_lat    = str(issue['lat']),
            geo_long   = str(issue['lon']),
        )


        rss_items.append( item )

    rss = GeoRSS.GeoRSS(
        title         = "FixMyStreet Game",
        link          = request.build_absolute_uri(),
        description   = "Foo",
        lastBuildDate = datetime.datetime.now(),
        items         = rss_items,
    )
    
    return HttpResponse(
        content = rss.to_xml(),
        content_type = 'application/rss+xml'
    )
