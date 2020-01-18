from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    link = models.URLField(verbose_name='Direccion Web', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')#Se ejecuta cada vez que se registra
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')#Se ejecuta cada vez que se actualiza

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]#ordenar la lista de proyectos el "-" es para ordenarlo del primero al ultimo o biceversa
        
    def __str__(self):
        return self.title#cambia el nombre el titulo del proyecto para no mn