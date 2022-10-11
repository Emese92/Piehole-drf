from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    prep_time = models.PositiveSmallIntegerField(
        help_text="Enter time in minutes", blank=True, null=True)
    number_of_portions = models.PositiveIntegerField()
    ingredients = models.TextField(help_text="One ingedient per line")
    steps = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_swtmii',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
