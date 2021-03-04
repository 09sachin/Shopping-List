from django.db import models
from django.contrib.auth.models import User

status = [('Pending', 'Pending'), ('Bought', 'Bought'), ('Not Available', 'Not Available')]


class Shopping_list(models.Model):
    item_name = models.CharField(max_length=500)
    item_quantity = models.CharField(max_length=100)
    item_status = models.CharField(max_length=100, choices=status)
    date = models.DateField()
    person = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.person.username

    class Meta:
        verbose_name = 'Shopping list'
        verbose_name_plural = 'Shopping list'

