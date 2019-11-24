from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .forms import *


# Create your views here.
def index(request):
    return render(
        request,
        'index.html'
    )


class registerView(CreateView):
    form_class = SimpleUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
