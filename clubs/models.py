from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Age(models.Model):

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Club(models.Model):

    class Meta:
        verbose_name_plural = 'Clubs'

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    age = models.ForeignKey(
        'Age', null=True, blank=True, on_delete=models.SET_NULL)
    teacher = models.CharField(max_length=254, null=True, blank=True)
    term = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
