from django.conf.urls import url,include
from . import views





urlpatterns = [

    url(r'^$',views.home_page,name='homepage'),

    url(r'^details/(?P<id>\w{0,50})/$',views.todo_details,name='tododetails'),

    url(r'^add/',views.add_todos,name='add_todos'),
    url(r'^login/$',views.login_page , name='login'),
    url(r'^register/$',views.register , name='register'),

]