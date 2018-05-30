from django.shortcuts import render
from django.http import HttpResponse

from .models import Company
from taggit.models import Tag
# Create your views here.
def index(request):
    all_companies = Company.objects.order_by('-pub_date')
    all_tags = Tag.objects.all().order_by('name')
    context = {'all_companies':all_companies,
                'all_tags' : all_tags,}
    return render(request, 'database/index.html', context)


def search(request):
    # check if request contains query and that query is not empty
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        filtered = Company.objects.filter(company_name__icontains = query)
        context = {'all_companies':filtered}
        return render(request, 'database/index.html', context)
    return index(request)

def filter_by_tag(request):
    if 'tag' in request.GET and request.GET['tag']:
        tags = [request.GET['tag']]
        filtered = Company.objects.filter(company_tags__name__in = tags)
        context = {'all_companies' : filtered}
        return render(request, 'database/index.html', context)
    return index(request);

def filter_by_size(request):
    if 'slider' in request.GET and request.GET['slider']:
        minNum = request.GET['slider']
        # gte = greater than equal to
        filtered = Company.objects.filter(number_of_employee__gte = minNum)
        context = {'all_companies' : filtered}
        return render(request, 'database/index.html', context)
    return index(request);

def query(request):
    query_filtered = []
    tag_filtered = []
    slider_filtered = []
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        query_filtered = Company.objects.filter(company_name__icontains = query)
    if 'tag' in request.GET and request.GET['tag']:
        tags = [request.GET['tag']]
        tag_filtered = Company.objects.filter(company_tags__name__in = tags)
    if 'slider' in request.GET and request.GET['slider']:
        minNum = request.GET['slider']
        # gte = greater than equal to
        slider_filtered = Company.objects.filter(number_of_employee__gte = minNum)
    filtered = union(query_filtered, tag_filtered)
    filtered = union(filtered, slider_filtered)
    if filtered == []:
        print('here')
        return index(request)
    else:
        print(filtered)
        context = {'all_companies' : filtered}
        return render(request, 'database/index.html', context)

def union(l1, l2):
    result = [i for i in l1]
    temp = [i for i in l2]
    for i2 in l2:
        for t in temp:
            if i2 == t:
                temp.remove(i2)
    result.append(l2)
    return result
