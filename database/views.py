from django.shortcuts import render
from django.http import HttpResponse

from .models import Company
# Create your views here.
def index(request):
    all_companies = Company.objects.order_by('-pub_date')
    context = {'all_companies':all_companies}
    return render(request, 'database/index.html', context)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']
        filtered = Company.objects.filter(company_name__icontains = query)
        context = {'all_companies':filtered}
        return render(request, 'database/index.html', context)
    return index(request)
