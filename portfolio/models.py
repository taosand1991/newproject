from django.db import models
from django.shortcuts import reverse

# Create your models here.
CATEGORY_CHOICES = (
    ('BS', 'Business cards'),
    ('Fl', 'Flyers'),
    ('LG', 'Logos'),
    ('IF', 'Infographics'),
)


class Personal(models.Model):
    name = models.CharField(max_length=200, )
    email = models.EmailField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='personal/', blank=True, null=True)
    categories = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='BS')

    def get_absolute_url(self):
        return reverse('port-detail', args=[self.pk])

