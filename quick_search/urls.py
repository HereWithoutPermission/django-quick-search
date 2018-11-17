from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('js', views.get_js, name='get_js'),
    path('css', views.get_css, name='get_css'),
    path('html', views.get_html, name='get_html'),
]
