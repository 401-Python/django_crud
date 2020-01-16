from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Player
from django.urls import reverse_lazy
# Create your views here.
class PlayerListView(ListView):
  model = Player
  template_name = 'home.html'

class PlayerDetailView(DetailView):
  model = Player
  template_name = 'players.html'  

class PlayerCreateView(CreateView):
  model = Player
  template_name = 'create_players.html'
  fields = ['player_name', 'height', 'weight', 'position', 'author']

class PlayerDeleteView(DeleteView):
  model = Player
  template_name = 'delete_players.html'
  success_url = reverse_lazy('home')

class PlayerUpdateView(UpdateView):
  model = Player
  template_name = 'edit_players.html'
  fields = ['player_name', 'height', 'weight', 'position']
