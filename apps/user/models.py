# django
from django.db import models
from django.contrib.auth.models import User
# third
# own

# Create your models here.

ROL_CHOICES = (
    ('AMD', u'Administrador'),
)

class UserApp(models.Model):
    '''
    Esta clase se encarga de definir los actributos de la tabla Usuario de la base de datos ryvatec.
    '''
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    usuid = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__
        return self.name

    class Meta:
        verbose_name = "UserApp"
        verbose_name_plural = "UsersApp"