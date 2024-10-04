from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'parents'

    def __str__(self):
        return self.name

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('parent', 'name')
        verbose_name_plural = 'children'

    def __str__(self):
        return self.name
    

