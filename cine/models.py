from django.db import models

class Peliculas(models.Model):
    titulo   = models.CharField(max_length=200)
    duracion = models.DurationField()
    reparto  = models.TextField()
    director = models.CharField(max_length=200)
    genero   = models.CharField(max_length=200)
    idioma   = models.CharField(max_length=200)
    imagen   = models.ImageField(upload_to = os.path.join(BASE_DIR))
    modalidad = models.IntegerField(default = 0)
    cartelera = models.BooleanField(default = False)

    def titulo(self):
        return self.titulo
    def duracion(self):
        return self.duracion
    def idioma(self):
        return self.idioma



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text