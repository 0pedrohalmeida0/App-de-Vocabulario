from django.db import models

# Create your models here.

class Palavra(models.Model): 
    termo = models.CharField(max_length=100)
    significado = models.TextField()
    exemplo = models.TextField(blank=True, null=True)
    idioma = models.CharField(max_length=5, default='pt-br')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'palavras'

    def __str__(self):
        return self.termo
