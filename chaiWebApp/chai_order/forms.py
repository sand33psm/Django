from django import forms
from .models import ChaiVariety

class ChaiOrderForm(forms.ModelForm):
    class Meta:
        model = ChaiVariety
        fields = ['name', 'date', 'type', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700'}),
            'date': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700', 'id': 'date-picker'}),
            'type': forms.Select(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700'}),
            'image': forms.ClearableFileInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700'}),

        }
        labels = {
            'name': 'Chai Name',
            'date': 'Order Date',
            'type': 'Chai Type',
            'image': 'Chai Image'
        }
        