from django.urls import path

from .views import PlayerListView, PlayerDetailView, PlayerCreateView, PlayerDeleteView, PlayerUpdateView

urlpatterns = [
  path('players/<int:pk>/', PlayerDetailView.as_view(), name='players'),
  path('', PlayerListView.as_view(), name='home'),
  path('players/new/', PlayerCreateView.as_view(), name='player_new'),
  path('players/delete/<int:pk>', PlayerDeleteView.as_view(), name='player_delete'),
  path('players/<int:pk>/edit/', PlayerUpdateView.as_view(), name='player_edit'),

]