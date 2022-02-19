from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .models import Post
from django.utils.text import slugify
from magazine.forms import EmailForMagazineForm
# from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
# from .forms import SearchForm

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 9) # 9 posts in each page
    page = request.GET.get('page')
    email_form=EmailForMagazineForm()
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
         posts = paginator.page(paginator.num_pages)
    return render(request,'articles/list.html',{'page': page,'posts': posts,'email_form':email_form})

# def post_detail(request, year, month, day, post):
    # myslug = slugify(post , allow_unicode=True)
    # post = get_object_or_404(Post, status='published',publish__year=year,publish__month=month,publish__day=day,slug=myslug)
    # return render(request,'articles/detail.html',{'post': post})


def post_detail(request,post):
    post = get_object_or_404(Post, slug=post,status='published')
    return render(request,'articles/detail.html',{'post': post})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 6
    form_class = EmailForMagazineForm,
    template_name = 'articles/list.html'


# def post_search(request):
#     form = SearchForm()
#     query = None
#     results = []
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['query']
#         results = Post.published.annotate(
#         search=SearchVector('title', 'body'),).filter(search=query)
#         return render(request,'articles/search.html',{'form': form,'query': query, 'results': results})
#     search_vector = SearchVector('title', 'body')
#     search_query = SearchQuery(query)
#     results = Post.published.annotate(search=search_vector,rank=SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank')


# menus

def vegetation_cover(request):
    return render(request,'menus/rs_farming/vegetation_cover.html')

def precision_agriculture(request):
    return render(request,'menus/rs_farming/precision_agriculture_products.html')

def object_detection(request):
    return render(request,'menus/rs_farming/object_detection.html')

def mapping(request):
    return render(request,'menus/geodezy/mapping.html')

def subsidence(request):
    return render(request,'menus/disaster/subsidence.html')

def flood(request):
    return render(request,'menus/disaster/flood.html')

def toolbox(request):
    return render(request,'menus/gis/arcpy.html')

def siteselection(request):
    return render(request,'menus/gis/siteselection.html')

def work(request):
    return render(request,'menus/workWithUs.html')

def about(request):
    return render(request,'menus/aboutus.html')