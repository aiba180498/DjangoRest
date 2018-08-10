from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    zakazchik = models.CharField(max_length=250, null=True)
    Otpravitel = models.CharField(max_length=250, null=True)
    Poluchatel = models.CharField(max_length=250, null=True)
    kolichestvo = models.IntegerField(blank=True, null=True)
    ves = models.IntegerField(blank=True, null=True)
    obem = models.IntegerField(blank=True, null=True)
    upakovka = models.CharField(max_length=250, null=True)
    brak = models.ImageField(upload_to='Blog/', blank=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.title)
