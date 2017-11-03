from django.conf.urls import url
from . import views

app_name = 'kingapp'

urlpatterns = [
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'kingapp/(\d+)/$', views.detail, name='detail'),
    url(r'index/', views.index, name='index'),

]


