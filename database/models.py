from django.db import models
from datetime import date
# Create your models here.
from taggit.managers import TaggableManager
class Company(models.Model):
    company_name = models.CharField(("Company Name"),max_length = 200)
    pub_date = models.DateField(("Publish Date"), default=date.today)
    number_of_employee = models.IntegerField(("Number of Employees"), default = 1)
    company_website = models.URLField(("Company Website"), default = "https://www.google.com/")
    company_email = models.EmailField(blank = True)
    company_description = models.TextField(default = "No Description Available")
    company_image_url = models.URLField(("Company Image URL"), default = "http://www.gladessheriff.org/media/images/most%20wanted/No%20image%20available.jpg")
    company_tags = TaggableManager()

    def __str__(self):
        return self.company_name
