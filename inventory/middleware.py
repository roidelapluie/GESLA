from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
import re

class SiteLogin:
    "This middleware requires a login for every view"
    def process_request(self, request):
        if request.user.is_anonymous() and \
        (not re.match('/media', request.path) and \
        not re.match('/login', request.path) and \
        not re.match('/logout', request.path)):
            if request.POST:
                return login(request)
            else:
                return HttpResponseRedirect('/login?next=%s' % (request.path))

