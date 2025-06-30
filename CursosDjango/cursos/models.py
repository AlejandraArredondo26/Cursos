from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Name") 
    descripcion = models.TextField(verbose_name="Desc")           
    duracion = models.IntegerField(verbose_name="plazo")     
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="cost")  
    activo = models.BooleanField(default=True, verbose_name="state") 
    imagen = models.ImageField( null=True, upload_to='fotos', verbose_name="img")     
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="created")   
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="modified")

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['fecha_creacion']  

    def __str__(self):
        return self.nombre  
    
    