from django import forms
from .models import Gamers  # Import the Gamers model

class GamerForm(forms.ModelForm):
    game_hours = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'number'}))
    
    class Meta:
        model = Gamers  # Use the model class, not an instance
        fields = ['gamer_tag', 'email', 'econtact', 'game_hours']


    