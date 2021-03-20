from django import forms
from .models import TModel

class TForm(forms.ModelForm):
	class Meta:
		model=TModel
		fields='__all__'

