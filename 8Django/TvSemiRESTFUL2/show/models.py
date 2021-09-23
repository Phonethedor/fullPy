from django.db import models

# Create your models here.


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['title']) < 5:
            errors["title"] = "Title should be at least 5 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network name should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Description of the show should be at least 10 characters"
        return errors
    pass


class Show(models.Model):
    title = models.CharField(default="Title*", max_length=255)
    network = models.CharField(default="Network*", max_length=255)
    release_date = models.DateField()
    description = models.TextField(default="Description*")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"Show ID: ({self.id})| Title: {self.title}| Network: {self.network}| Release Date: {self.release_date}| Description: {self.description} ||"