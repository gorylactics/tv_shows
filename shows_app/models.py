from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def validacion(self, postData):
        errores={}
        fecha = datetime.now().strftime('%Y-%m-%d')

        if len(postData['title']) < 2:
            errores['len_title'] = 'Title debe tener como minimo 5 caracteres'

        if len(postData['network']) < 3:
            errores['len_network'] = 'El largo minimo de Network debe ser de 3 caracteres'
            
        if len(postData['description']) < 10:
            errores['len_description'] = 'La descripcion debe tener a lo menos 15 caracteres'

        if postData['release_date'] >= fecha:
            errores['release_date'] = f'La fecha no puede ser igual o futura a hoy {fecha}'
        return errores

class Show(models.Model):
    title = models.CharField(max_length = 100)
    network = models.CharField(max_length = 100)
    description = models.TextField(max_length = 255)
    release_date = models.DateField()#asi guarda solo la fecha que manualmete se ingrsa, no hora ni mins 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = ShowManager()

    def __repr__(self):
        return f'id: {self.id}\ntitle: {self.title}\nnetwork: {self.network}\ndescription: {self.description}\nrelease date: {self.release_date}'
    def __str__(self):
        return f'id: {self.id}\ntitle: {self.title}\nnetwork: {self.network}\ndescription: {self.description}\nrelease date: {self.release_date}'
