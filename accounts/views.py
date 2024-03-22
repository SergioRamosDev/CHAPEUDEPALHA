from django.shortcuts import render
from django.contrib.auth.forms import UserCreationform
from django.urls import reverse_lazy
from django.views import generic



class SignUp(generic.CreateView):
    form_class = UserCreationform
    success_url = reverse_lazy('login')
    template_name = 'registration/register.hmtl'
