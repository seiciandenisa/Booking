from django.db import models


# Create your models here.
class FirstTable(models.Model):
    instance = models.CharField(max_length=100)
    content = models.TextField()


# class History(models.Model):
#     instance = models.ForeignKey(FirstTable, on_delete=models.CASCADE)
#     date_modified = models.DateTimeField(auto_now=True)
#     old_content = models.TextField()
