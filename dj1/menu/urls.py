from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


app_name = 'menu'
urlpatterns = [
    # ex: /menu/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/$', views.CategoryView.as_view(), name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/$',
        views.cat_detail, name='cat_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
