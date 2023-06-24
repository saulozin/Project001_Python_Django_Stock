from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    sector = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.registration} - {self.user.first_name}'
    
    def clean(self):
        pass