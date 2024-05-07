from django.db import models

class Districk(models.model):
    id_distrik = models.AutoField(primary_key=True)
    nama_distrik = models.CharField(max_Length=30)
    
    def __str__(self):
        return self.nama_distrik

class Kampung(models.Model):
    id_kampung = models.AutoField(primary_key=True)
    distrik = models.Foreignkey(Districk, on_delete=models.CASCADE)
    nama_kampung = model.CharField(max_Length=30)

    def __str__(self):
        return self.nama_kampung