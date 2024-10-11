from django.db import models
from django.utils import timezone

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'Masala'),
        ('GR', 'Ginger'),
        ('KL', 'Kiwi'),
        ('PL', 'Plain'),
        ('EL', 'Elaichi'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_images')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)

    def __str__(self):
        return self.name