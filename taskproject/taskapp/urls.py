from django.urls import path
from . import views
app_name='taskapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('log',views.log,name='log'),
    path('regis',views.regis,name='regis'),
    path('lout',views.lout,name='lout'),
    path('allcat',views.allcat,name='allcat'),
    path('detail',views.detail,name='detail'),
    path('load-branches',views.load_branches,name='ajax_load_branches'),
    path('info',views.info,name='info')
    # path('new',views.neww,name='neww')


]