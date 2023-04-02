from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    Lat = models.FloatField()
    Lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)


