from django import forms
from .models import TModel

class TForm(forms.ModelForm):
	class Meta:
		model=TModel
		fields='__all__'

		widgets ={'task' : forms.Textarea(attrs={'rows':6,'cols':80, 
			'style':'resize:none','placeholder':'Write Tasks Here'}),
			'tno':forms.NumberInput(attrs={'placeholder':'Task No '})}

