from django.db import models

# Create your models here.
class Company(models.Model):
    idno = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255,default='sagar.com')
    year_founded = models.IntegerField(null=True,blank=True)
    industry = models.CharField(max_length=255,default='Technology')
    size_range = models.CharField(max_length=50,default='not specified')
    locality = models.CharField(max_length=255,default='dharangaon')
    country = models.CharField(max_length=255,default='india')
    linkedin_url = models.URLField(max_length=255,default='default')
    current_employee_estimate = models.PositiveIntegerField(default=786)
    total_employee_estimate = models.PositiveIntegerField(default=786)

    def __str__(self):
        return self.name
