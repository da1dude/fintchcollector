from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #this is our route for the index page of fintches
    path('finches/', views.finches_index, name='index'),
    #route for the detail page of our finches
    #we need an id as well as a way to refer to the id(a route paramater)
    path('finches/<int:finch_id>', views.finches_detail, name='detail')
]