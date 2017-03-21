from django.conf.urls import url
from . import views

app_name = 'books'
urlpatterns = [
    # ex: /books/
    url(r'^$', views.index, name='index'),
    # ex: books/5/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: books/author/5/
    url(r'^author/(?P<author_id>[0-9]+)/$',
        views.author_detail, name='author_detail'),
    url(r'^search-form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
]
