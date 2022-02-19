from django.urls import path,re_path
from . import views
app_name = 'articles'
urlpatterns = [
# post views
        path('articles/', views.PostListView.as_view(), name='post_list'),
        # path('<int:year>/<int:month>/<int:day>/<str:post>/',
        #     views.post_detail,
        #     name='post_detail'),

        re_path(r'detail/(?P<post>[-\w]+)/', views.post_detail, name='post_detail'),
        # add post with form
        # path("add", views.create_article, name="create_article"),
        # path('search/', views.post_search, name='post_search'),
        
]

