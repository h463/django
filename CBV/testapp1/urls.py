from django.conf.urls import url
from . import views
urlpatterns = [

    url(r"^$", views.CompanyListView.as_view(), name="list"),
    url(r'^create/', views.CompanyCreateView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.CompanyDetailView.as_view(), name="detail"),
    url(r'^update/(?P<pk>\d+)/$', views.CompanyUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', views.CompanyDeleteView.as_view()),

]