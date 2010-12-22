import urlparse
import urllib2

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

import settings

@login_required
def issue(request, issue_id=None):
    if request.method == 'POST':
        target_url = urlparse.urljoin(settings.FMS_URL, '/report/%s' % issue_id)
        data =  {'submit_update': '1',
                 'id': issue_id,
                 'name': request.User.get_full_name(),
                 'email': request.User.email,
                 'rznvy': '', # check this
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
        response = urllib2.open(target_url, data)
        # FIXME handle the response    
        return HttpResponseRedirect(reverse('geolocate'))
    return render_to_response('issue.html')

    