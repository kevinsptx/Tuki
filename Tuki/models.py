from django.db import models

class Pelicula(models.Model):
    pelicula=models.CharField(max_length=100)
    fecha=models.DateField(auto_now_add=True)
    calificacion=models.IntegerField()
    comentario=models.TextField(blank=True)

    def __str__(self):
        return self.pelicula
