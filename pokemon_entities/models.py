from django.db import models


class Pokemon(models.Model):
    title = models.CharField('Название (рус.)', max_length=200, blank=True)
    title_en = models.CharField('Название (англ.)', max_length=200, blank=True)
    title_jp = models.CharField('Название (яп.)', max_length=200, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True, verbose_name='Изображение покемона')
    description = models.TextField('Описание', blank=True)
    previous_evolution = models.ForeignKey(
        "Pokemon",
        on_delete=models.SET_NULL,
        verbose_name='Предыдущая эволюция',
        null=True,
        blank=True,
        related_name="next_evolutions",
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pokemon}: {self.latitude}, {self.longitude}"
