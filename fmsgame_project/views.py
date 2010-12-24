import urlparse
import urllib2
import urllib
import cgi

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

import fixmystreet
import datetime
import GeoRSS

import settings
from scoreboard import models as scoreboard_models

from BeautifulSoup import BeautifulSoup

states = {'notfound': 'Not Found',
          'fixed': 'Fixed',
          'notfixed': 'Not Fixed',
          }

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
            new_points = 1
        elif state == 'notfixed':
            data['update'] = 'fmsgame: this is not fixed'
            new_points = 1
        elif state == 'notfound':
            data['update'] = "fmsgame: this couldn't be found"
            new_points = 1
        else:
            raise Http404

        response = urllib2.urlopen(target_url, urllib.urlencode(data))

        score_obj, created = scoreboard_models.Score.objects.get_or_create(user=request.user)
        old_score = score_obj.score or 0
        score_obj.score = old_score + new_points
        score_obj.save()

        request.session['last_issue_id'] = issue_id
        request.session['last_issue_status'] = state

        # FIXME handle the response    
        return HttpResponseRedirect(reverse('geolocate'))

    fms_url = 'http://www.fixmystreet.com/report/%s/' %(issue_id)
    fms_response = urllib2.urlopen(fms_url)

    fms_soup = BeautifulSoup(fms_response.read())
    google_maps_link = fms_soup.find('p', {'id': 'sub_map_links' }).a['href']

    split_link = urlparse.urlsplit(google_maps_link)
    useful_string = cgi.parse_qs(split_link.query)['q'][0]
    target_lat, target_long = useful_string.rsplit(None, 1)[1].split('@')[1].split(',')
    issue_summary = fms_soup.find('div', {'id': 'side'}).find('p', {'align': 'right'}).findPrevious('p').string

    extra_context = {
        'target_lat': target_lat, 
        'target_long': target_long,
        'issue_id': issue_id,
        'issue_title': fms_soup.title.string,
        'issue_summary': issue_summary,
        'last_issue_status': states.get(request.session.get('last_issue_status')),
        }

    context = context_instance=RequestContext(request)

    last_issue_id = request.session.get('last_issue_id')

    if issue_id == request.session.get('last_issue_id'):
        template = 'issue_done.html'
    else:
        template = 'issue.html'

    return render_to_response(template, extra_context, context)

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

        description_start = '<h2><a href="' + issue_url + '">Follow me to play</a></h2><br><br>'

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

def scoreboard(request):
    scores = scoreboard_models.Score.objects.all().order_by('-score')
    context = RequestContext(request)
    if request.user.is_authenticated():
        try:
            user_score = request.user.score_set.all()[0].score
        except IndexError:
            # This is because the user doesn't have a score yet. Use zero.
            user_score = 0

        my_range = range(user_score)
    else:
        user_score = None
        my_range = []
    my_range = range(user_score)
    return render_to_response('scoreboard.html', {'scores': scores, 'score': user_score, 'range': my_range}, context) 

