from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('',views.landing,name='landing'),
    path('searchz',views.search_results, name='search_results'),
    path('category', views.page_category,name='page_category'),
    path('location', views.page_location,name='page_location'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)