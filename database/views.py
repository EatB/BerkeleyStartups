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
    # all_tags = Tag.objects.all().order_by('name')
    # check if request contains query and that query is not empty
    if 'search' in request.GET and request.GET['search']:
        query = request.GET['search']
        filtered = Company.objects.filter(company_name__icontains = query)
        # context = {'all_companies':filtered,
        #             'all_tags' : all_tags,}
        return filtered
    #     return render(request, 'database/index.html', context)
    # return index(request)

def filter_by_tag(request):
    # all_tags = Tag.objects.all().order_by('name')
    if 'tag' in request.GET and request.GET['tag']:
        tags = request.GET.getlist("tag")
        filtered = Company.objects.filter(company_tags__name__in = tags)
        # context = {'all_companies':filtered,
        #             'all_tags' : all_tags,}
        return filtered
        #     return render(request, 'database/index.html', context)
        # return index(request);

def filter_by_size(request):
    # all_tags = Tag.objects.all().order_by('name')
    if 'slider' in request.GET and request.GET['slider']:
        minNum = request.GET['slider']
        # gte = greater than equal to
        filtered = Company.objects.filter(number_of_employee__gte = minNum)
        # context = {'all_companies':filtered,
        #             'all_tags' : all_tags,}
        return filtered

def query(request):
    all_tags = Tag.objects.all().order_by('name')
    search_filtered = search(request) # search_filtered = None when no search entered
    tag_filtered = filter_by_tag(request)
    size_filtered = filter_by_size(request)
    filtered = size_filtered
    if(search_filtered != None):
        filtered = filtered & search_filtered
    if(tag_filtered != None):
        filtered = filtered & tag_filtered
        # querysets = [c.company_tags.all() for c in filtered]
        # user_entered_tag_names = []
        # if 'tag' in request.GET and request.GET['tag']:
        #     user_entered_tag_names = [request.GET['tag']]
        # for qs in querysets:
        #     for t in qs:
        #         for name in user_entered_tag_names:
        #             if t.name == name and t not in selected_tags:
        #                 selected_tags.append(t)

    selected_tags = request.GET.getlist("tag")
    context = {'all_companies':filtered,
                'all_tags' : all_tags,
                'selected_tags': selected_tags,}

    return render(request, 'database/index.html', context)
