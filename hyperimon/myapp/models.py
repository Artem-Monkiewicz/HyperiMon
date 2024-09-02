from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    roof_length = models.FloatField()
    roof_width = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Panel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='panels')
    length = models.FloatField()
    width = models.FloatField()
    quantity = models.IntegerField()