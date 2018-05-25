from django.contrib import admin

from .models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'pub_date','number_of_employee', 'company_website', 'company_description']
    list_filter = ['pub_date', 'number_of_employee']
    search_fields = ['company_name', 'company_description']

admin.site.register(Company, CompanyAdmin)
