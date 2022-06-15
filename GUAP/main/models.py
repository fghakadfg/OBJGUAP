from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
# Create your models here.


class Upload(models.Model):
    File = models.FileField(upload_to='media/')
    Text = models.CharField("Название", max_length=250)
    date = models.DateField('Дата')






