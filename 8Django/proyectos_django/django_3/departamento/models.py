from django.db import models

class Departamento(models.Model):
    num_dpto = models.IntegerField()
    direccion = models.CharField(max_length=200)
    numero_calle = models.IntegerField()
    comuna = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=10)

def __str__(self):
    return str(self.codigo_postal)