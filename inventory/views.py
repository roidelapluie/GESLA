from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Object, Manufacturer

def index(request):
    objects = Object.objects.filter(reference_person=request.user,
        end_date__isnull=True)
    closed_objects = Object.objects.filter(reference_person=request.user,
        end_date__isnull=False)
    return render_to_response('gesla/index.html', { 'objects': objects,
        'closed_objects': closed_objects },
        context_instance=RequestContext(request))

def all(request):
    objects = Object.objects.filter(end_date__isnull=True)
    closed_objects = Object.objects.filter(end_date__isnull=False)
    return render_to_response('gesla/index.html', { 'objects': objects,
        'closed_objects': closed_objects },
        context_instance=RequestContext(request))

def manufacturer_all(request):
    manufacturers = Manufacturer.objects.all()
    return render_to_response('gesla/manufacturers.html', { 'manufacturers': \
        manufacturers }, context_instance=RequestContext(request))

def manufacturer_view(request, manufacturer_id):
    manufacturer = \
        Manufacturer.objects.get(id=manufacturer_id)
    objects = Object.objects.filter(manufacturer=manufacturer)
    return render_to_response('gesla/manufacturer.html', { 'objects': \
        objects, 'manufacturer': manufacturer },
        context_instance=RequestContext(request))

def object_view(request, object_id):
    selected_object = \
        Object.objects.get(id=object_id)
    if selected_object.reference_person != request.user and \
        not request.user.is_staff:
        selected_object = None
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
