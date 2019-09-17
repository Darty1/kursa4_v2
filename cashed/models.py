from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Named(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Priced(models.Model):
    class Meta:
        abstract = True

    price = models.DecimalField(max_digits=8, decimal_places=2)


class City(models.Model):
    class Meta:
        abstract = True
    city = models.CharField(max_length=100)


class Bonus(Named, Priced, City):
    img = models.ImageField(upload_to='companys', null=True)
    description_of_bonus = models.TextField(null=True)
    date = models.DateField(null=True)
    count = models.IntegerField(max_length=None, null=True)


class Company(Named, Priced):
    image = models.ImageField(upload_to='companys', null=True)
    description = models.TextField(null=True)
    date_of_end = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE, null=True)

class Consumer(models.Model):
    class Meta(User.Meta):
        verbose_name = 'consumer'
        verbose_name_plural = 'consumers'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    wish_list = models.ManyToManyField(Company)
