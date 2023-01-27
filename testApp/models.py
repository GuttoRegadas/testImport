from django.db import models

# Create your models here.
class EmailTeste(models.Model):
    email = models.CharField(max_length= 150 ,verbose_name="E-mail")

    def __str__(self):
        return f'{self.email}'