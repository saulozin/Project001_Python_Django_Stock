from django import forms
from app.models import Product, Category, Supplier
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
        ),
        required=False,
    )

    class Meta:
        model = Product

        fields = (
            'code', 'name', 'serial_number', 'registration_date', 'validate_date', 'quantity',
            'location', 'description', 'category', 'supplier', 'picture', 
        )

    def clean_code(self):
        code = self.cleaned_data.get('code')
        current_code = self.instance.code

        if current_code != code:
            if Product.objects.filter(code=code).exists():
                self.add_error(
                    'code',
                    ValidationError(
                        'Este código já existe.',
                        code='invalid'
                    )
                )

        return code
    

class CategoryForm(forms.ModelForm): 
    class Meta:
        model = Category

        fields = (
            'category_name',
        )

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        current_category_name = self.instance.category_name

        if current_category_name != category_name:
            if Category.objects.filter(category_name=category_name).exists():
                self.add_error(
                    'category_name',
                    ValidationError(
                        'Este nome de categoria já existe.',
                        code='invalid'
                    )
                )

        return category_name


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier

        fields = (
            'supplier_code', 'supplier_name',
        )

    def clean_supplier_code(self):
        supplier_code = self.cleaned_data.get('supplier_code')
        current_supplier_code = self.instance.supplier_code

        if current_supplier_code != supplier_code:
            if Supplier.objects.filter(supplier_code=supplier_code).exists():
                self.add_error(
                    'supplier_code',
                    ValidationError(
                        'Este código de fornecedor já existe.',
                        code='invalid'
                    )
                )

        return supplier_code