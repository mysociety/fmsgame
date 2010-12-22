from django.shortcuts import render_to_response

def issue(request, issue_id=None):
    if request.method == 'post':
        pass
    return render_to_response('issue.html')

    