from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect

@login_required
def issue(request, issue_id=None):
    if request.method == 'post':
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

    