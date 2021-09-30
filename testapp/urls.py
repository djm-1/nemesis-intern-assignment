from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.alluser,name='allusers'),
    path('',include('django.contrib.auth.urls')),
    path('delete/<int:id>',views.deleteuser,name='deleteuser'),
    path('signup',views.signup,name='signup')
]
