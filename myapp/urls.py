from django.urls import path

from . import views

urlpatterns=[
    path('',view=views.home,name='home'),
    path('test',view=views.test,name='test'),
    path('review',view=views.review,name='review'),
    path('allreview',view=views.allreview,name='allreview'),
]