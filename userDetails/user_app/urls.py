from django.urls import path
#from . import views
from user_app import views
#Template naming ..
app_name='userBasicApp'
urlpatterns=[
   path('relative/',views.relative,name='relative'),
   path('other/',views.other,name='other'),
   path('basic/',views.basic,name='basic')
]
