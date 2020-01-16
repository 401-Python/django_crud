from django.db import models
from django.urls import reverse
positions = (
  ('1', 'PG'),
  ('2', 'SG'),
  ('3', 'SF'),
  ('4', 'PF'),
  ('5', 'C'),
)
# Create your models here.
class Player(models.Model):
   player_name = models.CharField(max_length=50)
   author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
   height = models.DecimalField(max_digits=4, decimal_places=2)
   weight = models.DecimalField(max_digits=5, decimal_places=2)
   position = models.CharField(max_length=20, choices=positions, default='water boy')

   def __str__(self):
     return self.player_name
    
   def get_absolute_url(self):
     return reverse('players', args=[self.id])