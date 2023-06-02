from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'


class QueryForm(forms.Form):
    latitude = forms.FloatField(label='Latitude', help_text='Enter latitude as a float value')
    longitude = forms.FloatField(label='Longitude', help_text='Enter longitude as a float value')
    distance = forms.FloatField(label='Distance (in kilometers)')
