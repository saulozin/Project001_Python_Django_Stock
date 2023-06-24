from django import forms
from app.models import Product
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError

class StockForm(forms.ModelForm):
    registration_date = forms.DateField(widget=DateInput(format='%d/%m/%Y'), help_text='Format dd/mm/yyyy')
    validate_date = forms.DateField(widget=DateInput(format='%d/%m/%Y'), help_text='Format dd/mm/yyyy')
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs= {
                'accept': 'image/*',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.fields['code'].widget.attrs.update({
        #    'placeholder' : 'Codigo do produto'
        #})

    class Meta:
        model = Product

        fields = (
            'code', 'name', 'registration_date', 'validate_date', 'quantity',
            'location', 'description', 'category', 'supplier', 'picture', 
        )

        #Alterar os componentes do formulario dinamicamente de acorso com o Model
        #widgets = {
        #    'code': forms.TextInput(
        #        attrs = {
        #            'placeholder' : 'Codigo do produto'
        #        }
        #    )
        #}

    #def clean(self):
        #cleaned_data = self.cleaned_data
        #print(cleaned_data.get('code'))
        #return super().clean()
    
