from django.db import models

class ShowManager(models.Manager):
    def validacion(self, postData):
        errores={}
        if len(postData['title']) < 5:
            errores['len_title'] = 'el largo de title es minimo 5'
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
