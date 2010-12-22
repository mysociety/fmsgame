from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def issue(request, issue_id=None):
    if request.method == 'post':
        pass
    return render_to_response('issue.html')

    