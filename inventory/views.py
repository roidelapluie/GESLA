from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Object

def index(request):
    objects = Object.objects.filter(reference_person=request.user)
    return render_to_response('gesla/index.html', { 'objects': objects },
        context_instance=RequestContext(request))

def all(request):
    objects = Object.objects.all()
    return render_to_response('gesla/index.html', { 'objects': objects },
        context_instance=RequestContext(request))

def object_view(request, object_id):
    selected_object = \
        Object.objects.get(id=object_id)
    if selected_object.reference_person != request.user:
        selected_object = None
#        filter(reference_person=request.user)
    return render_to_response('gesla/object.html', { 'object': \
        selected_object }, context_instance=RequestContext(request))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    infos = []
    errors = []
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        next_page = 'gesla/index.html'
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()

    return render_to_response('gesla/auth.html', {
        'form': form, 'errors': errors, 'infos': infos,
    }, context_instance=RequestContext(request))
