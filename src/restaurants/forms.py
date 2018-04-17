from django import forms

from .models import RestaurantLocation
from .validators import validate_country


class RestaurantLocationCreateForm(forms.ModelForm):
	COUNTRY = forms.CharField(required=False, validators=[validate_country])
	
	class Meta:
		model = RestaurantLocation
		fields = [
			'name',
			'location',
			'category',
		]