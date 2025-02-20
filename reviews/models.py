from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviwes')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação inválida. Tem que ser maior que 0.'),
            MaxValueValidator(5, 'Avaliação inválida. Tem que ser menor que 0.'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie
