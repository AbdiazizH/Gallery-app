from django.conf.urls import url
from . import views

urlpatterns=[
   url('^$',views.home,name = 'home'),
    url('^category/$',views.catergory,name='catergory'),
     url('^nature/$',views.nature,name='nature'),
     url('^travel/$',views.travel,name='travel'),
     url('^animals/$',views.animals,name='animals'),
     url('^food/$',views.food,name='food'),
     url('^work/$',views.work,name='work'),
     url('^search/$',views.search_results,name='search'),
]