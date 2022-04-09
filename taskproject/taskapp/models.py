from django.db import models
from django.urls import reverse


class branch(models.Model):
    name = models.CharField(max_length=300)
    add = models.URLField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'


    def __str__(self):
        return self.name

class place(models.Model):
    pname= models.CharField(max_length=250)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)

    class Meta:
         ordering = ('pname',)
         verbose_name = 'place'
         verbose_name_plural = 'places'

    def __str__(self):
        return self.pname


class item(models.Model):
    product=models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(blank=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('product',)
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return '{}'.format(self.product)


class userdetail(models.Model):
    name=models.CharField(max_length=250)
    ph=models.IntegerField()
    email=models.TextField(unique=False)
    add=models.TextField()
    prod = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    quantity=models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    delivery=models.DateTimeField(auto_now_add=False)
    class Meta:
        db_table = 'userdetail'


    def __str__(self):
        return '{}'.format(self.name)

# class demo(models.Model):
#     name=models.CharField(max_length=250)

