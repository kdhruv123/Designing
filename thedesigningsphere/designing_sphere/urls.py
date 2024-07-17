from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('contact',views.contact, name = 'contact'),
    path('graphic',views.graphic, name = 'graphic'),
    path('project',views.project, name = 'project'),
    path('dhruv',views.dhruv, name = 'dhruv'),
    path('dhruv/moreinfo', views.dm, name='moreinfo'),
    path('gautam',views.gautam, name = 'gautam'),
    path('gautam/moreinfo',views.gm, name = 'moreinfo'),
    path('teaser',views.teaser, name = 'teaser'),
    path('teaser/surabhi', views.surabhi, name='surabhi'),
    path('teaser/samyak', views.samyak, name='samyak'),
    path('teaser/dandiya', views.dandiya, name='dandiya'),
    path('teaser/carnival', views.carnival, name='carnival'),
    path('teaser/ram-aagman', views.ram, name='ram'),
    path('teaser/reel-samyak', views.reel, name='reel'),
    path('CGI',views.cgi, name = 'CGI'),
    path('team',views.team, name = 'team'),
    path('submit_query', views.submit_query, name='submit_query'),
]