from django.shortcuts import render
from django.views.generic import DetailView,ListView,TemplateView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

from .models import Snack

# Create your views here.

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack

class SnackDetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack

class HomePage(TemplateView):
    template_name = 'home.html'

class snackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['name','description','purchaser','img_url']

class snackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['name','description','purchaser','img_url']

class snackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snacks')
    


