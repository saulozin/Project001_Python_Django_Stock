import os
from PIL import Image
from django.conf import settings
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.utils.text import slugify

#https://docs.djangoproject.com/pt-br/4.2/topics/db/models/
#https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-choices
# Create your models here.

#id(Primary Key - pk), name(str), code(str), registration_date(date), validate_date(date), quantity(int), location(str),
#description(text), picture(image), supplier(fk), category(fk)

#É a tabela, servira para criar, atualizar e excluir dados da base de dados

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    category_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.category_name}'

    
class Supplier(models.Model):
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    supplier_code = models.CharField(max_length=50)
    supplier_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.supplier_name}'


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, blank=True)
    registration_date = models.DateField()
    validate_date = models.DateField()
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, blank=True, null=True)

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}-{self.code}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.picture:
            self.resize_image(self.picture, max_image_size)

    def clean(self):
        error_messages = {}
        code_enviado = self.code or None
        code_salvo = None
        product = Product.objects.filter(code=code_enviado).first()

        if product:
            code_salvo = product.code
            if code_salvo is not None and self.pk != product.pk:
                error_messages['code'] = 'Código de produto já existe.'

        if error_messages:
            raise ValidationError(error_messages)


    def __str__(self) -> str:
        return f'{self.code} - {self.name}'
    

