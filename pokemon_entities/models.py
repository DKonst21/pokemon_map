from django.db import models


class Pokemon(models.Model):
    title = models.CharField('Название (рус.)', max_length=200)
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
        return self.title

    class Meta:
        verbose_name = 'Тип покемона'
        verbose_name_plural = 'Типы покемонов'


class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey("Pokemon",
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name="entities",
                                verbose_name='Тип покемона')
    appeared_at = models.DateTimeField(null=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(null=True, verbose_name='Время исчезновения')
    level = models.IntegerField(blank=True, null=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='Сила')
    defence = models.IntegerField(blank=True, null=True, verbose_name='Зашита')
    stamina = models.IntegerField(blank=True, null=True, verbose_name='Выносливость')

    def __str__(self):
        return f"{self.pokemon}: {self.latitude}, {self.longitude}"

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'
