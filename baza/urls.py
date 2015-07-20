from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^firma/(?P<pk>\d+)$', views.FirmaDetailView.as_view(), name='firma-detail'),
    url(r'^add_firma/', views.add_firma, name='add-firma'),
]
