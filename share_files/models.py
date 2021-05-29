from django.db import models



class Post(models.Model):
    compartido_por = models.CharField(max_length=100, null=True, blank=True)
    nombre_del_archivo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='files')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_del_archivo + '/' + self.compartido_por
    
