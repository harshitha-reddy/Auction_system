

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from classviews import *
from Auction_system.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'Auction_system/index.html')

